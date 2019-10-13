from django import forms
from django.shortcuts import render, redirect

from fibest.models.company import Company

# Probando Héctor.
from django.views.generic import CreateView

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ("login", "name", "link")

        help_texts = {
            'link': 'Website of the company. Example: https://www.fibest.org.',
        }


def index(request):
    if request.method == "GET":
        try:
            company = Company.objects.get(id=request.session["id"])
            form = CompanyForm(instance=company)
            return render(request, "inscription.html", {"form": form})
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
        except:
            form = CompanyForm(request.POST)
            if form.is_valid():
                company = form.save(commit=False)
                company.login_code = 'AAA'
                company.save()
        finally:
            return redirect("/dashboard/")