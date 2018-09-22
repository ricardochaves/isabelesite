
from django.shortcuts import render

from htmlmin.decorators import minified_response
from mainapp.models import Address
from mainapp.models import ComplexServices
from mainapp.models import Deposition
from mainapp.models import Index
from mainapp.models import SimpleServices


@minified_response
def index(request):
    home = Index.objects.first()
    depositions = Deposition.objects.all()
    address = Address.objects.all()

    response = render(request, "mainapp/index.html", {"home": home, "depositions": depositions, "address": address})
    response["Cache-Control"] = "public, max-age=10, stale-while-revalidate=2592000, stale-if-error=2592000"

    return response


@minified_response
def services(request):
    home = Index.objects.first()
    simple_services = SimpleServices.objects.all()
    complex_services = ComplexServices.objects.all()

    menu_url = True

    response = render(
        request,
        "mainapp/services.html",
        {"home": home, "simple_services": simple_services, "complex_services": complex_services, "menu_url": menu_url},
    )
    response["Cache-Control"] = "public, max-age=10, stale-while-revalidate=2592000, stale-if-error=2592000"

    return response
