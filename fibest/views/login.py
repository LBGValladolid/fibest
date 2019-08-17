from django.shortcuts import render, redirect
from fibest.models.company import Company

import random
import string

from fibest.services import mail

def login(request):
    if request.method == "GET":
        if "code" in request.GET:
            company = Company.objects.get(login=request.GET["email"])
            code = request.GET["code"]
            if company.login_code == code:
                request.session["id"] = company.id
                return redirect("/dashboard/")
            else:
                return render(request, "login.html", {"error_message": "Incorrect credentials"})
        else:
            return render(request, "login.html")
    elif request.method == "POST":
        email = request.POST["email"]
        try:
            company = Company.objects.get(login=email)
            letters = string.ascii_letters
            code = ''.join(random.choice(letters) for i in range(15))
            company.login_code = code
            company.save()
            send_login_mail(email, code)
        except Company.DoesNotExist:
            # CREAR COMPAÑIA NUEVA
            return redirect("/inscription/")
    else:
        return

def send_login_mail(email, code):
    url = f"https://fibest.org/login/?email={email}&code={code}"
    mail.send_mail([email], "Login to FiBEST", f"""<h1>Login to FiBEST</h1>

Please, click on the following link to login to FiBEST website: <a href="{url}">{url}</a>
"""
    )