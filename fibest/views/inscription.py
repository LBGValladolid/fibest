from django.shortcuts import render, redirect
from django.forms import ModelForm

from fibest.models.company import Company

class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ("login", "name", "link")

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