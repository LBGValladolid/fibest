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
        if m:
            m_list = [m.publi_magazine,
                      m.name_magazine, m.activity_magazine, m.search_magazine, m.year_magazine, m.workers_magazine,
                      m.location_magazine, m.internships_magazine, m.beca_magazine, m.tfg_magazine, m.web_contact,
                      m.email_contact, m.person_contact, m.phone_contact, m.postal_contact, m.twitter, m.facebook,
                      m.instagram,
                      m.youtube, m.linkedin, m.message_magazine]
        else:
            m_list = [None] * 21

        if s:
            s_list = [s.publi_stand,
                      s.name_stand, s.activity_stand, s.search_stand, s.year_stand, s.workers_stand,
                      s.location_stand, s.internships_stand, s.beca_stand, s.tfg_stand, s.web_contact,
                      s.email_contact, s.person_contact, s.phone_contact, s.postal_contact, s.twitter, s.facebook,
                      s.instagram,
                      s.youtube, s.linkedin, s.message_stand]
        else:
            s_list = [None] * 21

        writer.writerow(
            [c.name, c.login, c.link, c.logo, c.stand_name, c.assembly_service, c.cvs_requested] + m_list + s_list)

        return response