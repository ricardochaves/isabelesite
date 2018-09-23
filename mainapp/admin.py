from django.contrib import admin
from image_cropping import ImageCroppingMixin

from mainapp.models import Address
from mainapp.models import Coaching
from mainapp.models import ComplexServices
from mainapp.models import Deposition
from mainapp.models import Index
from mainapp.models import Psychology
from mainapp.models import SimpleServices


class IndexAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass


admin.site.register(Index, IndexAdmin)
admin.site.register(ComplexServices)
admin.site.register(Deposition)
admin.site.register(Address)
admin.site.register(SimpleServices)
admin.site.register(Psychology)
admin.site.register(Coaching)
