from django import forms
from tinymce.widgets import TinyMCE

from django.shortcuts import render, redirect

from fibest.models.company import Stand, Company

# TODO: no guarda bien

class StandForm(forms.ModelForm):

    class Meta:
        model = Stand
        fields = ("email_contact", "person_contact", "phone_contact", "postal_contact", "twitter", "facebook", "instagram", "youtube", "message_stand", )

def index(request):
    if request.method == "GET":
        try:
            Company.objects.get(id=request.session["id"])
            try:
                stand = Stand.objects.get(company=request.session["id"])
                form = StandForm(instance=stand)
                return render(request, "stand.html", {"form": form})
            except:
                form = StandForm()
                return render(request, "stand.html", {"form": form})
        except Exception as e:
            print(str(e))
            return redirect("/login")
    elif request.method == "POST":
        try:
            stand = Stand.objects.get(company=request.session["id"])
            form = StandForm(request.POST, instance=stand)
            if form.is_valid():
                form.save()
        except:
            form = StandForm(request.POST, request.FILES)
            print(form.errors)
            if form.is_valid():
                stand = form.save(commit=False)
                stand.company = Company.objects.get(id=request.session["id"])
                stand.save()
        finally:
            return redirect("/dashboard")