from django import forms
from django.shortcuts import render, redirect

from fibest.models.company import Company


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ("logo", "stand_name", "cvs_requested", "assembly_service")
        widgets = {
            'cvs_requested': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
        }


def index(request):
    if request.method == "GET":
        try:
            company = Company.objects.get(id=request.session["id"])
            form = CompanyForm(instance=company)
            return render(request, "forum.html", {"form": form})
        except Exception as e:
            print(str(e))
            return redirect("/login")
    elif request.method == "POST":
        company = Company.objects.get(id=request.session["id"])

        if request.FILES.get('logo', None) is not None:
            request.FILES['logo'].name = company.name + ".jpg"
        form = CompanyForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            form.save()
            return redirect("/dashboard")
        else:
            return render(request, 'magazine.html', {'form': form})
