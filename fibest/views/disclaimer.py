from django.shortcuts import render, redirect
from fibest.models.company import  Company


def index(request):
    try:
        Company.objects.get(id=request.session["id"])
        return render(request, "disclaimerText.html")
    except Exception as e:
        return redirect("/login")


