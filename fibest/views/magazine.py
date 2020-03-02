from django import forms
from django.shortcuts import render, redirect

from fibest.models.company import Magazine, Company


class MagazineForm(forms.ModelForm):
    #Añadido para cancelar la edición (Tambien quitado el botón en el form) (Y en el js de tinymce)
    def __init__(self, *args, **kwargs):
        super(MagazineForm, self).__init__(*args, **kwargs)
        for field in self.fields.keys():
            self.fields[field].disabled = True
    class Meta:
        model = Magazine
        exclude = ["company"]


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
        company = Company.objects.get(id=request.session["id"])
        if request.FILES.get('publi_magazine', None) is not None:
            request.FILES['publi_magazine'].name = company.name + ".jpg"

        try:
            magazine = Magazine.objects.get(company=request.session["id"])
            form = MagazineForm(request.POST, request.FILES, instance=magazine)
            print(form)
            if form.is_valid():
                form.save()
                return redirect("/")
            else:
                return render(request, 'magazine.html', {'form': form})

        except:
            form = MagazineForm(request.POST, request.FILES)
            if form.is_valid():
                magazine = form.save(commit=False)
                magazine.company = Company.objects.get(id=request.session["id"])
                magazine.save()
                return redirect("/")
            else:
                return render(request, 'magazine.html', {'form': form})
