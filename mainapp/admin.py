from django.contrib import admin


from mainapp.models import ModelExample
from mainapp.models import Index

from image_cropping import ImageCroppingMixin


class ModelExampleAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass


admin.site.register(ModelExample, ModelExampleAdmin)
admin.site.register(Index)
