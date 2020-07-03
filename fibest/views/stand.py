from django import forms
from django.shortcuts import render, redirect

from fibest.models.company import Stand, Company, Magazine


class StandForm(forms.ModelForm):
    #Añadido para cancelar la edición (Tambien quitado el botón en el form) (Y en el js de tinymce)
    def __init__(self, *args, **kwargs):
        super(StandForm, self).__init__(*args, **kwargs)
        for field in self.fields.keys():
            self.fields[field].disabled = True
    class Meta:
        model = Stand
        exclude = ["company"]


def index(request):
    if request.method == "GET":
        try:
            Company.objects.get(id=request.session["id"])
            try:
                magazine = Magazine.objects.get(company=request.session["id"])
            except:
                magazine = None
            try:
                stand = Stand.objects.get(company=request.session["id"])
                form = StandForm(instance=stand)
                return render(request, "stand.html", {"form": form, "magazine": magazine})
            except:
                form = StandForm()
                return render(request, "stand.html", {"form": form, "magazine": magazine})
        except Exception as e:
            print(str(e))
            return redirect("/login")
    elif request.method == "POST":

        myRequest = request.POST.copy()
        if request.POST.get("copy_magazine_info"):
            magazine = Magazine.objects.get(company=request.session["id"])
            myRequest["name_stand"] = magazine.name_magazine
            myRequest["activity_stand"] = magazine.activity_magazine
            myRequest["search_stand"] = magazine.search_magazine
            myRequest["year_stand"] = magazine.year_magazine
            myRequest["workers_stand"] = magazine.workers_magazine
            myRequest["location_stand"] = magazine.location_magazine
            myRequest["internships_stand"] = magazine.internships_magazine
            myRequest["beca_stand"] = magazine.beca_magazine
            myRequest["tfg_stand"] = magazine.tfg_magazine
            myRequest["web_contact"] = magazine.web_contact
            myRequest["email_contact"] = magazine.email_contact
            myRequest["person_contact"] = magazine.person_contact
            myRequest["phone_contact"] = magazine.phone_contact
            myRequest["postal_contact"] = magazine.postal_contact
            myRequest["twitter"] = magazine.twitter
            myRequest["facebook"] = magazine.facebook
            myRequest["instagram"] = magazine.instagram
            myRequest["youtube"] = magazine.youtube
            myRequest["message_stand"] = magazine.message_magazine

        try:
            stand = Stand.objects.get(company=request.session["id"])
            form = StandForm(myRequest, instance=stand)
            if form.is_valid():
                form.save()
                return redirect("/")
            else:
                return render(request, 'stand.html', {'form': form})

        except:
            form = StandForm(myRequest, request.FILES)
            print(form.data)
            if form.is_valid():
                stand = form.save(commit=False)
                stand.company = Company.objects.get(id=request.session["id"])
                stand.save()
                return redirect("/")
            else:
                return render(request, 'stand.html', {'form': form})
