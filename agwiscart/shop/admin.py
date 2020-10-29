from django.contrib import admin
from shop.models import product,category,subcategory,productimages
from django.contrib.contenttypes.admin import GenericTabularInline
from import_export.admin import ImportExportModelAdmin
# from imagekit.admin import AdminThumbnail
# Register your models here.
class ImageInline(GenericTabularInline):
    model = productimages

@admin.register(product)
class productAdmin(ImportExportModelAdmin):
    list_filter = ('category', 'subcategory')
    list_display = ("brand_name", "title","category","subcategory","sell_price","active")

@admin.register(productimages)
class productimagesAdmin(ImportExportModelAdmin):
    # image_tag = AdminThumbnail(image_field='image')
    # image_tag.short_description = 'Image'
    list_display =("image_tag","product","active","timestamp")
    readonly_fields=[('image_tag')]

    # fields =("image","product","active","timestamp")

@admin.register(category)
class categoryAdmin(ImportExportModelAdmin):
    ordering=['title']
    list_display =("category_id","title")

@admin.register(subcategory)
class subcategoryAdmin(ImportExportModelAdmin):
    ordering=['subcategory_id']
    list_display =("subcategory_id","category","title","timestamp")
    