from django.shortcuts import render, redirect
from fibest.models.company import Company, Forum


def index(request):
    try:
        company = Company.objects.get(id=request.session["id"])
        try:
            forum = Forum.objects.get(company=company)
        except Exception as e:
            print(str(e))
            forum = Forum.objects.create(company=company)
        return render(request, "dashboard.html", {"company": company, "forum": forum})
    except Exception as e:
        print(str(e))
        return redirect("/login")