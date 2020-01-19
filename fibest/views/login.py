import random
import string
import ssl

from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.translation import gettext as _

from fibest.models.company import Company


def login(request):
    if request.method == "GET":
        if "code" in request.GET:
            company = Company.objects.get(login=request.GET["email"])
            code = request.GET["code"]
            if company.login_code == code:
                request.session["id"] = company.id
                return redirect("/")
            else:
                return render(request, "login.html", {"error_message": "Incorrect credentials"})
        else:
            return render(request, "login.html", {"navButton": True})
    elif request.method == "POST":
        email = request.POST["email"]
        try:
            company = Company.objects.get(login=email)
            letters = string.ascii_letters
            code = ''.join(random.choice(letters) for i in range(15))
            company.login_code = code
            company.save()
            send_login_mail(email, code)
            return redirect("/")
        except Company.DoesNotExist:
            # CREAR COMPAÑIA NUEVA
            return redirect("/inscription/")
    else:
        return


def send_login_mail(email, code):
    context = ssl.create_default_context()

    url = f" https://empresas.fibest.org/login/?email={email}&code={code}"
    EmailMessage(
        subject=_("Login to FiBEST"),
        body=_("Please, click on the following link to login to FiBEST website:") + url,
        from_email='valladolid@sendinblue.com',
        to=[email],
        reply_to=['valladolid@best.eu.org'],
    ).send(fail_silently=False)


def logout(request):
    print(request.session.items())
    del request.session["id"]
    return JsonResponse({
        'success': True,
        'url': reverse('login')
    })
