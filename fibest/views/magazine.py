from django import forms
from tinymce.widgets import TinyMCE

from django.shortcuts import render, redirect

from fibest.models.company import Magazine, Company

class MagazineForm(forms.ModelForm):

    class Meta:
        model = Magazine
        fields = ("publi_magazine", "name_magazine", "activity_magazine", "search_magazine", "year_magazine", "workers_magazine", "location_magazine", "internships_magazine", "message_magazine")

def index(request):
    if request.method == "GET":
        try:
            Company.objects.get(id=request.session["id"])
            try:
                magazine = Magazine.objects.get(company=request.session["id"])
                form = MagazineForm(instance=magazine)
                return render(request, "magazine.html", {"form": form})
            except:
                form = MagazineForm()
                return render(request, "magazine.html", {"form": form})
        except Exception as e:
            print(str(e))
            return redirect("/login")
    elif request.method == "POST":
        try:
            magazine = Magazine.objects.get(company=request.session["id"])
            form = MagazineForm(request.POST, instance=magazine)

            if form.is_valid():
                form.save()
        except:
            form = MagazineForm(request.POST, request.FILES)
            if form.is_valid():
                magazine = form.save(commit=False)
                magazine.company = Company.objects.get(id=request.session["id"])
                magazine.save()
        finally:
            return redirect("/dashboard")