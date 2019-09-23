from django.contrib import admin

from base_site.mainapp.models import Address
from base_site.mainapp.models import Coaching
from base_site.mainapp.models import ComplexServices
from base_site.mainapp.models import Deposition
from base_site.mainapp.models import Index
from base_site.mainapp.models import Psychology
from base_site.mainapp.models import SimpleServices
from image_cropping import ImageCroppingMixin


class IndexAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass


admin.site.register(Index, IndexAdmin)
admin.site.register(ComplexServices)
admin.site.register(Deposition)
admin.site.register(Address)
admin.site.register(SimpleServices)
admin.site.register(Psychology)
admin.site.register(Coaching)
