import os
import random
import string
from secrets import token_urlsafe

from django import forms
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from fibest.models.company import Company


# Recordar de asignar la variable de entorno INSCRIPCION

class CompanyForm(forms.ModelForm):
    password = forms.CharField(label=_("password"), help_text=_("info password"), required=False,
                               widget=forms.PasswordInput)

    class Meta:
        model = Company
        fields = ("login", "name", "link", "pack", "hasVirtualStand",
                  "hasMagazine", "terms_confirmed")

        help_texts = {
            'terms_confirmed': mark_safe(
                str(_("Se aceptan la "))+"<a href='/privacy' target='_blank'%}>" + str(_('Privacy')) + "</a>")
        }


def index(request):
    if request.method == "GET":
        try:
            company = Company.objects.get(id=request.session["id"])
            form = CompanyForm(instance=company)
            return render(request, "inscription.html", {"form": form, "company": company})
        except:
            form = CompanyForm()
            return render(request, "inscription.html", {"form": form, "navButton": True})
    elif request.method == "POST":
        try:
            company = Company.objects.get(id=request.session["id"])
            form = CompanyForm(request.POST, instance=company)
            form.password = os.environ["INSCRIPCION"]
            print(form)
            if form.is_valid():
                company = form.save(commit=False)
                company.save()
                return redirect("/")
            else:
                print(form.errors)
                return render(request, 'inscription.html', {'form': form, "company": company})

        except:
            if request.POST["pack"] != "??":
                request.POST = request.POST.copy()
                request.POST["hasVirtualStand"] = True
                request.POST["hasMagazine"] = True
            form = CompanyForm(request.POST)
            if request.POST["password"] != os.environ["INSCRIPTION"]:
                form.add_error('password', _("passwords do not match !"))
                return render(request, 'inscription.html', {'form': form, "company": None})

            if not request.POST.get("terms_confirmed"):
                form.add_error('terms_confirmed', _("privacy not accepted"))

            if Company.objects.filter(login__exact = request.POST.get('login')).exists():
                form.add_error('login', _("Mail already registered"))

            if form.is_valid():
                company = form.save(commit=False)
                letters = string.ascii_letters
                code = ''.join(random.choice(letters) for i in range(15))
                company.login_code = code
                safe_name = request.POST["name"].encode(
                    "ascii", errors="ignore").decode()
                safe_name = (safe_name[:6]) if len(
                    safe_name) > 6 else safe_name
                tmpPk = safe_name + "_" + token_urlsafe(6)
                while Company.objects.filter(pk=tmpPk).exists():
                    pass
                company.id = tmpPk
                company.save()
                request.session["mail"] = request.POST.get('login')
                return redirect("login")
            else:
                return render(request, 'inscription.html', {'form': form, "company": None})
