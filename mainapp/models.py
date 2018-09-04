from django.db import models

from image_cropping import ImageRatioField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class ModelExample(models.Model):
    title = models.CharField(max_length=70, verbose_name='Title', default='', blank=True)
    image = models.ImageField(blank=True, upload_to='uploaded_images', verbose_name='Image')
    cropping = ImageRatioField('image', '430x360', verbose_name='Crop Image')
    active = models.BooleanField(verbose_name="Active", default=False)
    content = RichTextUploadingField("contents")


class Contact(models.Model):
    name = models.CharField(max_length=300, verbose_name="Name", blank=False, null=False)
    email = models.EmailField(verbose_name="E-Mail", blank=False, null=False)
    message = models.TextField(verbose_name="Message", blank=False, null=False)
