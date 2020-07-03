from django.shortcuts import render
from fibest.models.company import  Company


def index(request):
    try:
        Company.objects.get(id=request.session["id"])
        return render(request, "privacy.html")
    except Exception as e:
        return render(request, "privacy.html", {"navButton": True})

