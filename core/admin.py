from django.contrib import admin
from core.models import FontionBooks
# Register your models here.
class FontionBooksAdmin(admin.ModelAdmin):
    list_display = (
        # 'id',
        'productId',
        'productType',
        'imageUrl',
        'name',
        'currency',
        'sku',
        'urlSlug',
        'title',
        'author',
        # 'description',
        'price',
        'formatType',
       )
admin.site.register(FontionBooks,FontionBooksAdmin)
