import os

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from fibest.Storage.storage import OverwriteStorage


class Company(models.Model):
    id = models.CharField(max_length=16, primary_key=True)
    login = models.EmailField(
        _("Login email"),
        help_text=_("This mail will be used to login to FiBEST.")
    )
    login_code = models.CharField(max_length=15)
    name = models.CharField(
        _("Full name"),
        max_length=200,
        help_text=_("Full name of the company.")
    )

    link = models.URLField(
        _("Website"),
        help_text=_('Website of the company. Example: https://www.fibest.org.')
    )
    logo = models.ImageField(_("Logo"), help_text=_("Logo for the website, ideal size is 200x100 pixels"),
                             storage=OverwriteStorage(location=os.path.join(settings.MEDIA_ROOT, "logos"),
                                                      base_url=os.path.join(settings.MEDIA_URL, "logos")),
                             default=None)
    # Stand
    stand_name = models.CharField(_("Stand name"), max_length=200,
                                  help_text=_("Please indicate with what name exactly you want it to "
                                              "appear on the stand banner, on the maps of the job fair and "
                                              "in the schedules of activities. It will be case "
                                              "sensitive."), default="")

    assembly_service = models.BooleanField(_("Assembly service"), default=False,
                                           help_text=_("Based on the demands of companies participating in previous "
                                                       "editions, we also offer a service of "
                                                       "assembly of promotional material of your company, with a cost "
                                                       "of € 50 (this amount will be added "
                                                       "to the invoice of the job fair services). In this way, you simply "
                                                       "have to send the promotional "
                                                       "materials to the organization Two days in advance, and upon "
                                                       "arrival at the job fair they will all be "
                                                       "ready."))
    disclaimer = models.BooleanField(default=False)
    hasVirtualStand = models.BooleanField(_("Tiene stand virtual"), default=False, blank=True)
    hasMagazine = models.BooleanField(_("Tiene revista"), default=False, blank=True)
    cvs_requested = models.TextField(_("Curriculums"), max_length=2500, default="",
                                     help_text=_("Texto ayuda curriculums demandados"))
    terms_confirmed = models.BooleanField(_("terminos y condiciones"), default=False)

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
    pack = models.CharField(_("pack"), max_length=2, choices=PACKS, help_text=_("Ayuda para pack"))
    uploaded = models.BooleanField(_("Ha sido subido a fibest"), default=False, blank=True)


class Magazine(models.Model):
    company = models.ForeignKey(Company, models.CASCADE)
    publi_magazine = models.ImageField(_("Image for magazine"),
                                       storage=OverwriteStorage(location=os.path.join(settings.MEDIA_ROOT, "magazine"),
                                                                base_url=os.path.join(settings.MEDIA_URL, "magazine")),
                                       help_text=_("Your company will have a complete advertising page (image in size "
                                                   "A5) in the job fair magazine. To avoid pixelated problems in printing "
                                                   "would be convenient to send us this advertising sheet in format "
                                                   "vector, or with a minimum resolution of 300ppp (preferable in .png "
                                                   "format), avoiding if possible the format pdf. Remind them that the "
                                                   "size of the magazine is A5."))
    name_magazine = models.CharField(_("Name of the company magazine"), max_length=200)
    activity_magazine = models.CharField(_("Activity of the company"), max_length=500)
    search_magazine = models.CharField(_("What is your company looking for?"), max_length=2500)
    year_magazine = models.IntegerField(_("Year of foundation"), blank=True, null=True)
    workers_magazine = models.IntegerField(_("Number of workers"), blank=True, null=True)
    location_magazine = models.CharField(_("Location"), max_length=500, blank=True, null=True)
    internships_magazine = models.CharField(_("Magazine text for internships"), max_length=2500, blank=True, null=True)
    beca_magazine = models.CharField(_("Magazine text for becas"), max_length=2500, blank=True, null=True)
    tfg_magazine = models.CharField(_("Magazine text for TFGs"), max_length=2500, blank=True, null=True)

    web_contact = models.CharField(_("web contact"), max_length=200)
    email_contact = models.EmailField(_("email contact"))
    person_contact = models.CharField(_("person contact"), max_length=200)
    phone_contact = models.CharField(_("phone contact"), max_length=15)
    postal_contact = models.CharField(_("postal contact"), max_length=500)
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    message_magazine = models.TextField(_("message magazine"),
                                        help_text=_(
                                            "Text in which you have the opportunity to include detailed information "
                                            "about your mission, values, identity, offer of the company, "
                                            "current projects, success stories, selection process, etc. For guidance, "
                                            "the appropriate size of the Text would be approximately 1500 characters."))


class Stand(models.Model):
    company = models.ForeignKey(Company, models.CASCADE)
    copy_magazine_info = models.BooleanField(_("copy magazine info"), default=False,
                                             help_text=_("Info copia  datos revista"))

    name_stand = models.CharField(_("Name of the company"), max_length=200)
    activity_stand = models.CharField(_("Activity of the company virtual"), max_length=500)
    search_stand = models.CharField(_("What is your company looking for?"), max_length=2500)

    year_stand = models.IntegerField(_("Year of foundation"), blank=True, null=True)
    workers_stand = models.IntegerField(_("Number of workers"), blank=True, null=True)
    location_stand = models.CharField(_("Location"), max_length=500, blank=True, null=True)
    internships_stand = models.CharField(_("Magazine text for internships"), max_length=2500, blank=True, null=True)
    beca_stand = models.CharField(_("Magazine text for becas"), max_length=2500, blank=True, null=True)
    tfg_stand = models.CharField(_("Magazine text for TFGs"), max_length=2500, blank=True, null=True)
    web_contact = models.CharField(_("web contact"), max_length=200)
    email_contact = models.EmailField(_("email contact"))
    person_contact = models.CharField(_("person contact"), max_length=200)
    phone_contact = models.CharField(_("phone contact"), max_length=15)
    postal_contact = models.CharField(_("postal contact"), max_length=500)
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    message_stand = models.TextField(_("message vertual"), help_text=_(
        "Text in which you have the opportunity to include detailed information "
        "about your mission, values, identity, offer of the company, "
        "current projects, success stories, selection process, most searched "
        "profiles etc."))


class Forum(models.Model):
    company = models.ForeignKey(Company, models.CASCADE)

    # Contract data
    company_contract = models.CharField(_("Full name of the company."), max_length=500)
    cif_contract = models.CharField(_("CIF of the company."), max_length=15)
    signer_contract = models.CharField(
        _("Name of the person who will sign."), max_length=200)
    postal_contract = models.CharField(
        _("Address where we will send the contract."), max_length=2500)

    # Billing data
    company_billing = models.CharField(_("Full name of the company."), max_length=200)
    cif_billing = models.CharField(_("CIF  of the company."), max_length=15)
    postal_social_billing = models.CharField(_("postal social billing"), max_length=2500)
    phone_billing = models.CharField(_("Phone number for billing"), max_length=15)
    order_number = models.CharField(_("Order number"), max_length=30, default="", blank=True, null=True)
    postal_send_billing = models.CharField(_("Address where we will send the bill."), max_length=2500)

    # ENVIO DE MATERIAL (poner que van a enviar para que se lo podamos devolver)
    # ESTADO PAGO y CONTRATO
    # COMIDAS FIBEST
    # DESCARGAR CVs
    # SERVICIO NEWSLETTER
    # AVISOS POR CORREO PARA TODO (EMPRESAS(DLs, etc) y ALUMNOS (EVENTOS, ...))
    # REGISTRO
    # AVISO LEGAL
    # GDPR
