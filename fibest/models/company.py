from django.db import models

class Company(models.Model):
    login = models.EmailField()
    login_code = models.CharField(max_length=15)

    name = models.CharField(max_length=200)
    logo = models.ImageField()
    link = models.URLField()

    # PERFILES, tener checkboxes (MANY to MANY)

    # Magazine
    publi_magazine = models.ImageField()
    name_magazine = models.CharField(max_length=200)
    activity_magazine = models.CharField(max_length=500)
    search_magazine = models.CharField(max_length=2500)
    year_magazine = models.IntegerField()
    workers_magazine = models.IntegerField()
    location_magazine = models.CharField(max_length=500)
    internships_magazine = models.CharField(max_length=2500)
    message_magazine = models.TextField()

    #Contact
    email_contact = models.EmailField()
    person_contact = models.CharField(max_length=200)
    phone_contact = models.CharField(max_length=15)
    postal_contact = models.CharField(max_length=500)
    twitter = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    youtube = models.URLField(blank=True)

    # FiBEST Online
    message_stand = models.TextField()
    video_stand = models.URLField(blank=True)

    # Stand
    stand_name = models.CharField(max_length=200)

    # Contract data
    company_contract = models.CharField(max_length=500)
    cif_contract = models.CharField(max_length=15)
    signer_contract = models.CharField(max_length=200)
    postal_contract = models.CharField(max_length=2500)

    # Billing data
    company_billing = models.CharField(max_length=200)
    cif_billing = models.CharField(max_length=15)
    postal_social_billing = models.CharField(max_length=2500)
    phone_billing = models.CharField(max_length=15)
    postal_send_billing = models.CharField(max_length=2500)

    # PACK
    PACK_SPONSOR = "SP"
    PACK_SILVER = "SL"
    PACK_GOLD = "AU"
    PACK_PLATINUM = "PL"
    PACK_DIAMOND = "DI"
    PACK_CUSTOM = "??"
    PACKS = [
        (PACK_SPONSOR,"Sponsor"),
        (PACK_SILVER,"Silver"),
        (PACK_GOLD,"Gold"),
        (PACK_PLATINUM,"Platinum"),
        (PACK_DIAMOND,"Diamong"),
        (PACK_CUSTOM,"Custom")
    ]
    pack = models.CharField(max_length=2,choices=PACKS)

    # ENVIO DE MATERIAL (poner que van a enviar para que se lo podamos devolver)
    # ESTADO PAGO y CONTRATO
    # COMIDAS FIBEST
    # DESCARGAR CVs
    # SERVICIO NEWSLETTER
    # AVISOS POR CORREO PARA TODO (EMPRESAS(DLs, etc) y ALUMNOS (EVENTOS, ...))
    # REGISTRO
    # AVISO LEGAL
    # GDPR