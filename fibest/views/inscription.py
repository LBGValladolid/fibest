from django.shortcuts import render

from fibest.models.company import Company

def index(request):
    try:
        company = Company.objects.get(id=request.session["id"])
        return render(request, "inscription.html", {"company": company})
    except:
        return render(request, "inscription.html")