import os

from django import forms
from django.shortcuts import render, redirect

from fibest.models.company import Company

# Recordar de asignar la variable de entorno INSCRIPCION

class CompanyForm(forms.ModelForm):
    password = forms.CharField()

    def clean(self):
        cd = self.cleaned_data
        if cd.get('password') != os.environ["INSCRIPCION"]:
            self.add_error('password', "passwords do not match !")
        return cd

    class Meta:
        model = Company
        fields = ("login", "name", "link", "pack")

        help_texts = {
            'link': 'Website of the company. Example: https://www.fibest.org.',
        }


def index(request):
    if request.method == "GET":
        try:
            company = Company.objects.get(id=request.session["id"])
            form = CompanyForm(instance=company)
            return render(request, "inscription.html", {"form": form, "company": company})
        except:
            form = CompanyForm()
            return render(request, "inscription.html", {"form": form})
    elif request.method == "POST":
        try:
            company = Company.objects.get(id=request.session["id"])
            form = CompanyForm(request.POST, instance=company)
            if form.is_valid():
                company = form.save(commit=False)
                company.save()
                return redirect("/dashboard/")
            else:
                return render(request, 'inscription.html', {'form': form, "company": company})

        except:
            form = CompanyForm(request.POST)
            if form.is_valid():
                company = form.save(commit=False)
                company.login_code = 'AAA'
                company.save()
                return redirect("/dashboard/")
            else:
                return render(request, 'inscription.html', {'form': form, "company": None})
