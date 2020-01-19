from django import forms
from django.shortcuts import render, redirect

from fibest.models.company import Forum, Company


class ForumForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ("company_contract", "cif_contract", "signer_contract", "postal_contract",
                  "company_billing", "cif_billing", "postal_social_billing", "phone_billing", "order_number",
                  "postal_send_billing")


def index(request):
    if request.method == "GET":
        try:
            Company.objects.get(id=request.session["id"])
            try:
                forum = Forum.objects.get(company=request.session["id"])
                form = ForumForm(instance=forum)
                return render(request, "officialInformation.html", {"form": form})
            except Exception as e:
                print(e)
                form = ForumForm()
                return render(request, "officialInformation.html", {"form": form})
        except Exception as e:
            print(e)
            return redirect("/login")
    elif request.method == "POST":
        try:
            forum = Forum.objects.get(company=request.session["id"])
            form = ForumForm(request.POST, instance=forum)
            if form.is_valid():
                form.save()
        except:
            form = ForumForm(request.POST, request.FILES)
            if form.is_valid():
                forum = form.save(commit=False)
                forum.company = Company.objects.get(id=request.session["id"])
                forum.save()
        finally:
            return redirect("/")
