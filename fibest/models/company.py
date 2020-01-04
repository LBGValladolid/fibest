import os

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from fibest.Storage.storage import OverwriteStorage


class Company(models.Model):
    login = models.EmailField(
        "Login email",
        help_text="This mail will be used to login to FiBEST."
    )
    login_code = models.CharField(max_length=15)

    name = models.CharField(
        "Fullname",
        max_length=200,
        help_text="Fullname of the company."
    )

    link = models.URLField(
        "Website",
        help_text='Website of the company. Example: https://www.fibest.org.'
    )
    logo = models.ImageField("Logo", help_text="Logo for the website, ideal size is 200x100 pixels",
                             storage=OverwriteStorage(location=os.path.join(settings.MEDIA_ROOT, "logos"),
                                                      base_url=os.path.join(settings.MEDIA_URL, "logos")),
                             default=None)
    # Stand
    stand_name = models.CharField(max_length=200, help_text="Please indicate with what name exactly you want it to "
                                                            "appear on the stand banner, on the maps of the forum and "
                                                            "in the schedules of activities. It will be case "
                                                            "sensitive.", default="")

    assembly_service = models.BooleanField(default=False,
                                           help_text="Based on the demands of companies participating in previous "
                                                     "editions, we also offer a service of "
                                                     "assembly of promotional material of your company, with a cost "
                                                     "of € 50 (this amount will be added "
                                                     "to the invoice of the forum services). In this way, you simply "
                                                     "have to send the promotional "
                                                     "materials to the organization Two days in advance, and upon "
                                                     "arrival at the forum they will all be "
                                                     "ready.")
    disclaimer = models.BooleanField(default=False)
    hasVirtualStand = models.BooleanField(default=False)
    hasMagazine = models.BooleanField(default=False)

    # PACK
    PACK_SPONSOR = "SP"
    PACK_SILVER = "SL"
    PACK_GOLD = "AU"
    PACK_PLATINUM = "PL"
    PACK_DIAMOND = "DI"
    PACK_CUSTOM = "??"
    PACKS = [
        (PACK_SPONSOR, "Sponsor"),
        (PACK_SILVER, "Silver"),
        (PACK_GOLD, "Gold"),
        (PACK_PLATINUM, "Platinum"),
        (PACK_DIAMOND, "Diamond"),
        (PACK_CUSTOM, "Custom")
    ]
    pack = models.CharField(max_length=2, choices=PACKS, help_text=_("Ayuda para pack"))


class Magazine(models.Model):
    company = models.ForeignKey(Company, models.CASCADE)
    publi_magazine = models.ImageField("Image for magazine",
                                       storage=OverwriteStorage(location=os.path.join(settings.MEDIA_ROOT, "magazine"),
                                                                base_url=os.path.join(settings.MEDIA_URL, "magazine")),
                                       help_text="Your company will have a complete advertising page (image in size "
                                                 "A5) in the forum magazine. To avoid pixelated problems in printing "
                                                 "would be convenient to send us this advertising sheet in format "
                                                 "vector, or with a minimum resolution of 300ppp (preferable in .png "
                                                 "format), avoiding if possible the format pdf. Remind them that the "
                                                 "size of the magazine is A5.")
    name_magazine = models.CharField("Name of the company (magazine)", max_length=200)
    activity_magazine = models.CharField("Activity of the company (magazine)", max_length=500)
    search_magazine = models.CharField("What is your company looking for? (magazine)", max_length=2500)
    year_magazine = models.IntegerField("Year of foundation (magazine)",blank=True, null=True)
    workers_magazine = models.IntegerField("Number of workers (magazine)",blank=True, null=True)
    location_magazine = models.CharField("Location (magazine)", max_length=500,blank=True, null=True)
    internships_magazine = models.CharField("Magazine text for internships", max_length=2500, blank=True, null=True)
    beca_magazine = models.CharField("Magazine text for becas", max_length=2500, blank=True, null=True)
    tfg_magazine = models.CharField("Magazine text for TFGs", max_length=2500, blank=True, null=True)

    web_contact = models.CharField(max_length=200)
    email_contact = models.EmailField()
    person_contact = models.CharField(max_length=200)
    phone_contact = models.CharField(max_length=15)
    postal_contact = models.CharField(max_length=500)
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    message_magazine = models.TextField(
        help_text="Text in which you have the opportunity to include detailed information "
                  "about your mission, values, identity, offer of the company, "
                  "current projects, success stories, selection process, etc. For guidance, "
                  "the appropriate size of the Text would be approximately 300 words.")


class Stand(models.Model):
    company = models.ForeignKey(Company, models.CASCADE)
    copy_magazine_info = models.BooleanField(default=False, help_text=_("Info copia  datos revista"))

    name_stand = models.CharField("Name of the company", max_length=200)
    activity_stand = models.CharField("Activity of the company", max_length=500)
    search_stand = models.CharField("What is your company looking for?", max_length=2500)
    year_stand = models.IntegerField("Year of foundation", blank=True, null=True)
    workers_stand = models.IntegerField("Number of workers", blank=True, null=True)
    location_stand = models.CharField("Location", max_length=500, blank=True, null=True)
    internships_stand = models.CharField("Magazine text for internships", max_length=2500, blank=True, null=True)
    beca_stand = models.CharField("Magazine text for becas", max_length=2500, blank=True, null=True)
    tfg_stand = models.CharField("Magazine text for TFGs", max_length=2500, blank=True, null=True)
    web_contact = models.CharField(max_length=200)
    email_contact = models.EmailField()
    person_contact = models.CharField(max_length=200)
    phone_contact = models.CharField(max_length=15)
    postal_contact = models.CharField(max_length=500)
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    message_stand = models.TextField(help_text="Text in which you have the opportunity to include detailed information "
                                               "about your mission, values, identity, offer of the company, "
                                               "current projects, success stories, selection process, most searched "
                                               "profiles etc.")


class Forum(models.Model):
    company = models.ForeignKey(Company, models.CASCADE)

    # Contract data
    company_contract = models.CharField(max_length=500, help_text="Fullname of the company.")
    cif_contract = models.CharField("CIF", max_length=15, help_text="CIF of the company.")
    signer_contract = models.CharField("signer's name", max_length=200, help_text="Name of the person who will sign.")
    postal_contract = models.CharField("address", max_length=2500, help_text="Address where we will send the contract.")

    # Billing data
    company_billing = models.CharField(max_length=200, help_text="Fullname of the company.")
    cif_billing = models.CharField("Billing CIF", max_length=15)
    postal_social_billing = models.CharField(max_length=2500, help_text="Address where we will send the contract.")
    phone_billing = models.CharField("Phone number for billing", max_length=15)
    order_number = models.CharField("Order number", max_length=30, default="")
    postal_send_billing = models.CharField("billing address", max_length=2500,
                                           help_text="Address where we will send the bill.")

    # ENVIO DE MATERIAL (poner que van a enviar para que se lo podamos devolver)
    # ESTADO PAGO y CONTRATO
    # COMIDAS FIBEST
    # DESCARGAR CVs
    # SERVICIO NEWSLETTER
    # AVISOS POR CORREO PARA TODO (EMPRESAS(DLs, etc) y ALUMNOS (EVENTOS, ...))
    # REGISTRO
    # AVISO LEGAL
    # GDPR
