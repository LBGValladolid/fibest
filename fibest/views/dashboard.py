from django.shortcuts import render, redirect
from fibest.models.company import Company


def index(request):
    company = Company.objects.get(id=request.session["id"])
    return render(request, "dashboard.html", {"company": company})