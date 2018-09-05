from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.http import HttpResponseRedirect
from django.forms import modelform_factory

from mainapp.models import ModelExample
from mainapp.models import Index

from htmlmin.decorators import minified_response

# @requires_csrf_token


@cache_page(30)
@minified_response
def index(request):
    home = Index.objects.first()
    return render(request, "mainapp/index.html", {"home": home})
