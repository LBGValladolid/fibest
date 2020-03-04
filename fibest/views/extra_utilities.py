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
    writer.writerow([''])
    for c in company:
        m = magazine.filter(company=c.id).first()
        s = stand.filter(company=c.id).first()
        f = forum.filter(company=c.id).first()
        if c:
            c_fields = c._meta.fields
            tam = 21 - len(c_fields)
            c_list = []
            for f in c_fields:
                c_list += getattr(m, f)
            c_list = [None] * tam
        else:
            c_list = [None] * len(c._meta.fields)

        if m:
            m_fields = m._meta.fields
            tam = 21 - len(m_fields)
            m_list = []
            for f in m_fields:
                m_list += getattr(m, f)
            m_list = [None] * tam
        else:
            m_list = [None] * 21

        if s:
            s_fields = s._meta.fields
            tam = 21 - len(s_fields)
            s_list = []
            for f in s_fields:
                s_list += getattr(m, f)
            s_list = [None] * tam
        else:
            s_list = [None] * 21

        writer.writerow(
            c_list + m_list + s_list)

        return response
