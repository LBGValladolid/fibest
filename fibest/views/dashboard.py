from django.http import JsonResponse
from django.shortcuts import render, redirect
from fibest.models.company import Company, Forum


def index(request):
    try:
        company = Company.objects.get(id=request.session["id"])
        return render(request, "dashboard.html", {"company": company})
    except Exception as e:
        print(str(e))
        return redirect("/login")


def change_disclaimer(request):
    try:
        forum = Company.objects.get(id=request.session["id"])
        forum.disclaimer = True
        forum.save()

        return JsonResponse({"success": True})
    except Exception as e:
        return JsonResponse({"success": False})