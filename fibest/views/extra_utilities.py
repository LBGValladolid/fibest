import csv

from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse

from fibest.models.company import Company, Magazine, Stand, Forum


@permission_required('admin.can_add_log_entry')
def contact_download(request):
    company = Company.objects.all()
    magazine = Magazine.objects.all()
    stand = Stand.objects.all()
    forum = Forum.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="companies.csv"'
    writer = csv.writer(response, delimiter=',')
    field_names = []
    # c_fields = Company._meta.get_fields()
    # for f in c_fields:
    #     if f.__class__.__name__ is not "ManyToOneRel":
    #        field_names += [f.name]
    # m_fields = Magazine._meta.get_fields()
    # for f in m_fields:
    #     if f.__class__.__name__ is not "ManyToOneRel":
    #        field_names += [f.name]
    # s_fields = Stand._meta.get_fields()
    # for f in s_fields:
    #     if f.__class__.__name__ is not "ManyToOneRel":
    #        field_names += [f.name]
    fo_fields = Stand._meta.get_fields()
    for f in fo_fields:
        if f.__class__.__name__ is not "ManyToOneRel":
           field_names += [f.name]

    writer.writerow(
        field_names)
    for c in company:
        c_list = []
        m_list = []
        s_list = []
        f_list = []
        m = magazine.filter(company=c.id).first()
        s = stand.filter(company=c.id).first()
        f = forum.filter(company=c.id).first()
        # if c:
        #     c_fields = Company._meta.get_fields(include_hidden=True)
        #     tam = 15 - len(c_fields)
        #     for f in c_fields:
        #         if f.__class__.__name__ is not "ManyToOneRel":
        #             c_list += [getattr(c, f.name)]
        #             field_names += [f.name]
        #     c_list += [None] * tam
        # else:
        #     c_list = [None] * 15
        #
        # if m:
        #     m_fields = Magazine._meta.get_fields()
        #
        #     tam = 21 - len(m_fields)
        #     for f in m_fields:
        #         m_list += [getattr(m, f.name)]
        #         field_names += [f.name]
        #
        #     m_list += [None] * tam
        # else:
        #     m_list = [None] * 21
        #
        # if s:
        #     s_fields = Stand._meta.get_fields()
        #     tam = 21 - len(s_fields)
        #     for f in s_fields:
        #         s_list += [getattr(s, f.name)]
        #         field_names += [f.name]
        #
        #     s_list += [None] * tam
        # else:
        #     s_list = [None] * 21

        if s:
            f_fields = Stand._meta.get_fields()
            tam = 11 - len(f_fields)
            for f in f_fields:
                f_list += [getattr(s, f.name)]
                field_names += [f.name]

            f_list += [None] * tam
        else:
            f_list = [None] * 11

        writer.writerow(
                c_list + m_list + s_list + f_list)

    return response
