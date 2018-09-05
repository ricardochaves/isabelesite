from django.db import models

from image_cropping import ImageRatioField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class ModelExample(models.Model):
    title = models.CharField(max_length=70, verbose_name="Title", default="", blank=True)
    image = models.ImageField(blank=True, upload_to="uploaded_images", verbose_name="Image")
    cropping = ImageRatioField("image", "430x360", verbose_name="Crop Image")
    active = models.BooleanField(verbose_name="Active", default=False)
    content = RichTextUploadingField("contents")


class Contact(models.Model):
    name = models.CharField(max_length=300, verbose_name="Name", blank=False, null=False)
    email = models.EmailField(verbose_name="E-Mail", blank=False, null=False)
    message = models.TextField(verbose_name="Message", blank=False, null=False)


class Index(models.Model):
    title_about = models.CharField(
        max_length=30, verbose_name="Title Sobre", blank=False, null=False, help_text="Sobre"
    )
    text_about = models.TextField(verbose_name="Texto Sobre", blank=False, null=False)
    youtube_url = models.URLField(
        max_length=3000,
        verbose_name="YouTube Vídeo URL",
        help_text="https://www.youtube.com/embed/bEVO6klt3_o?rel=0&amp;showinfo=0",
    )
    whatsapp_api_url = models.URLField(
        max_length=3000,
        verbose_name="WhatsApp API URL",
        help_text="https://api.whatsapp.com/send?phone=5511992323959&amp;text=Acabei%20de%20ver%20o%20seu%20sit"
        "e%2C%20gostaria%20de%20mais%20informa%C3%A7%C3%B5es%20sobre...",
    )
    telfone = models.CharField(
        max_length=30, verbose_name="Telefone", blank=False, null=False, help_text="+55 11 9 7789-2344"
    )
    email = models.EmailField(verbose_name="E-Mail", blank=False, null=False, help_text="isabele@isabelelucchesi.com")
    email_subject = models.CharField(
        max_length=200,
        verbose_name="Assunto do E-mail",
        blank=False,
        null=True,
        help_text="Mais informações obre o tendimento.",
    )

    class Meta:
        verbose_name = "Home"
        verbose_name_plural = "Homes"

    def __str__(self):
        return self.title_about
