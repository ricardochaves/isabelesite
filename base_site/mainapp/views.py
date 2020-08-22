import random

from django.shortcuts import render
from django.views.decorators.cache import cache_page
from htmlmin.decorators import minified_response

from base_site.mainapp.models import Address
from base_site.mainapp.models import Coaching
from base_site.mainapp.models import ComplexServices
from base_site.mainapp.models import Deposition
from base_site.mainapp.models import Index
from base_site.mainapp.models import Psychology
from base_site.mainapp.models import SimpleServices
from base_site.settings import DJANGO_CACHE_VIEW_MINUTES


@cache_page(60 * DJANGO_CACHE_VIEW_MINUTES)
@minified_response
def index(request):

    home = Index.objects.first()
    depositions = Deposition.objects.all()
    final_depo = []

    if depositions:
        depositions = list(depositions)
        for i in range(3):  # pylint: disable=W0612
            elem = random.choice(depositions)
            depositions.remove(elem)
            final_depo.append(elem)

    address = Address.objects.all()

    response = render(request, "mainapp/index.html", {"home": home, "depositions": final_depo, "address": address})
    response["Cache-Control"] = "public, max-age=10, stale-while-revalidate=2592000, stale-if-error=2592000"

    return response


@minified_response
def psicologia(request):
    home = Index.objects.first()
    simple_services = SimpleServices.objects.filter(service=1).all()
    complex_services = ComplexServices.objects.filter(service=1).all()
    psychology = Psychology.objects.first()

    menu_url = True

    response = render(
        request,
        "mainapp/services.html",
        {
            "home": home,
            "simple_services": simple_services,
            "complex_services": complex_services,
            "menu_url": menu_url,
            "service": psychology,
        },
    )
    response["Cache-Control"] = "public, max-age=10, stale-while-revalidate=2592000, stale-if-error=2592000"

    return response


@minified_response
def coaching(request):
    home = Index.objects.first()
    simple_services = SimpleServices.objects.filter(service=2).all()
    complex_services = ComplexServices.objects.filter(service=2).all()
    coachings = Coaching.objects.first()
    menu_url = True

    response = render(
        request,
        "mainapp/services.html",
        {
            "home": home,
            "simple_services": simple_services,
            "complex_services": complex_services,
            "menu_url": menu_url,
            "service": coachings,
        },
    )
    response["Cache-Control"] = "public, max-age=10, stale-while-revalidate=2592000, stale-if-error=2592000"

    return response
