from django.db import models

class Company(models.Model):
    login = models.EmailField("Login email", help_text="This mail will be used to login to FiBEST")
    login_code = models.CharField(max_length=15)

    name = models.CharField("Name", max_length=200, help_text="Name of the company")
    link = models.URLField("Website", help_text="Website of the company")

class Magazine(models.Model):
    company = models.ForeignKey(Company, models.CASCADE)
    publi_magazine = models.ImageField("Image for magazine", help_text="Ideal size TBD")
    name_magazine = models.CharField("Name of the company (magazine)", max_length=200)
    activity_magazine = models.CharField("Activity of the company (magazine)", max_length=500)
    search_magazine = models.CharField("What is your company looking for? (magazine)", max_length=2500)
    year_magazine = models.IntegerField("Year of foundation (magazine)")
    workers_magazine = models.IntegerField("Number of workers (magazine)")
    location_magazine = models.CharField("Location (magazine)",max_length=500)
    internships_magazine = models.CharField("Magazine text for internships", max_length=2500)
    message_magazine = models.TextField("Magazine message (big text)")

class Stand(models.Model):
    company = models.ForeignKey(Company, models.CASCADE)
    email_contact = models.EmailField()
    person_contact = models.CharField(max_length=200)
    phone_contact = models.CharField(max_length=15)
    postal_contact = models.CharField(max_length=500)
    twitter = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    message_stand = models.TextField()
    video_stand = models.URLField(blank=True)

class Forum(models.Model):
    company = models.ForeignKey(Company, models.CASCADE)
    logo = models.ImageField("Logo", help_text="Logo for the website, ideal size is 200x100 pixels")
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