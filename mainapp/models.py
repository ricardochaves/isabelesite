# from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

from image_cropping import ImageRatioField
from storages.backends.gcloud import GoogleCloudStorage

# class ModelExample(models.Model):
#     title = models.CharField(max_length=70, verbose_name="Title", default="", blank=True)
#     image = models.ImageField(blank=True, upload_to="uploaded_images", verbose_name="Image")
#     cropping = ImageRatioField("image", "430x360", verbose_name="Crop Image")
#     active = models.BooleanField(verbose_name="Active", default=False)
#     content = RichTextUploadingField("contents")


# class Contact(models.Model):
#     name = models.CharField(max_length=300, verbose_name="Name", blank=False, null=False)
#     email = models.EmailField(verbose_name="E-Mail", blank=False, null=False)
#     message = models.TextField(verbose_name="Message", blank=False, null=False)

gs = GoogleCloudStorage()


class Index(models.Model):
    title_about = models.CharField(
        max_length=30, verbose_name="Título Sobre", blank=False, null=False, help_text="Sobre"
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
    title_depositions = models.CharField(max_length=200, verbose_name="Título Depoimentos", blank=False, null=True)
    title_contacts = models.CharField(max_length=200, verbose_name="Título Contatos", blank=False, null=True)
    title_enderecos = models.CharField(max_length=200, verbose_name="Título Endereços", blank=False, null=True)
    title_services = models.CharField(max_length=200, verbose_name="Título Serviços", blank=False, null=True)

    link_maps = models.URLField(
        max_length=1500,
        verbose_name="Url para o maps",
        help_text="https://www.google.com/maps/d/embed?mid=1PBARGGfXbqBOh_8T84kqYuz4qM87PJQW",
        null=True,
        blank=False,
    )

    link_facebook = models.URLField(max_length=1000, verbose_name="Facebook", null=True, blank=False)
    link_twitter = models.URLField(max_length=1000, verbose_name="Twitter", null=True, blank=False)
    link_linkedin = models.URLField(max_length=1000, verbose_name="Linkedin", null=True, blank=False)
    link_instagram = models.URLField(max_length=1000, verbose_name="Instagram", null=True, blank=False)

    image = models.ImageField(blank=True, null=True, upload_to="about_image", verbose_name="Imagem Sobre")
    cropping = ImageRatioField("image", "430x360", verbose_name="Crop Imagem Sobre")

    test = models.ImageField(blank=True, null=True, upload_to="teste", verbose_name="teste", storage=gs)

    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"

    def __str__(self):
        return self.title_about


class Deposition(models.Model):

    author = models.CharField(max_length=200, verbose_name="Autor", blank=False, null=False)
    text = models.CharField(max_length=2000, verbose_name="Texto", blank=False, null=False)

    class Meta:
        verbose_name = "Depoimento"
        verbose_name_plural = "Depoimentos"

    def __str__(self):
        return self.author


class SimpleServices(models.Model):
    text = models.CharField(max_length=2000, verbose_name="Texto", blank=False, null=False)

    class Meta:
        verbose_name = "Serviço Simples"
        verbose_name_plural = "Serviços Simples"

    def __str__(self):
        return self.text


class ComplexServices(models.Model):

    title = models.CharField(max_length=200, verbose_name="Título", blank=False, null=False)
    text = models.CharField(max_length=2000, verbose_name="Texto", blank=False, null=False)

    class Meta:
        verbose_name = "Serviço Complexo"
        verbose_name_plural = "Serviços Complexo"

    def __str__(self):
        return self.title


class Address(models.Model):

    title = models.CharField(max_length=400, verbose_name="Título", blank=False, null=False)
    text = models.CharField(max_length=2000, verbose_name="Texto", blank=False, null=False)

    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"

    def __str__(self):
        return self.title
