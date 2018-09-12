from django.contrib import admin

# from image_cropping import ImageCroppingMixin
# from mainapp.models import ModelExample
from mainapp.models import Address
from mainapp.models import ComplexServices
from mainapp.models import Deposition
from mainapp.models import Index
from mainapp.models import SimpleServices

# class ModelExampleAdmin(ImageCroppingMixin, admin.ModelAdmin):
#     pass


# admin.site.register(ModelExample, ModelExampleAdmin)
admin.site.register(Index)
admin.site.register(ComplexServices)
admin.site.register(Deposition)
admin.site.register(Address)
admin.site.register(SimpleServices)
