from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class FontionBooks(models.Model):
    productId = models.CharField(_("productId"), max_length=255,blank=True,null=True)
    productType = models.CharField(_("productType"), max_length=255,blank=True,null=True)
    imageUrl = models.URLField(_("Image URL"), max_length=256,blank=True,null=True)
    name = models.CharField(_("name"), max_length=255,blank=True,null=True)
    currency = models.CharField(_("currency"), max_length=100,blank=True,null=True)
    sku = models.CharField(_("currency"), max_length=100,blank=True,null=True)
    urlSlug = models.CharField(_("currency"), max_length=255,blank=True,null=True)
    title = models.CharField(_("title"), max_length=255,blank=True,null=True)
    author = models.CharField(_("author"), max_length=255,blank=True,null=True)
    description = models.TextField(_("description"),blank=True,null=True)
    price = models.DecimalField(_("price"), max_digits=6, decimal_places=2,blank=True,null=True)
    formatType = models.CharField(_("author"), max_length=255,blank=True,null=True)
