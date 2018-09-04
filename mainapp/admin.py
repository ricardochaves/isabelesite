from django.contrib import admin


from mainapp.models import ModelExample
from mainapp.models import Contact

from image_cropping import ImageCroppingMixin


class ModelExampleAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass


admin.register(ModelExample, ModelExampleAdmin)
admin.register(Contact)
