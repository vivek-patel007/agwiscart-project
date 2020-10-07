from django.contrib import admin
from shop.models import product,category,subcategory,productimages
from django.contrib.contenttypes.admin import GenericTabularInline
# from imagekit.admin import AdminThumbnail
# Register your models here.
class ImageInline(GenericTabularInline):
    model = productimages

@admin.register(product)
class productAdmin(admin.ModelAdmin):
    list_filter = ('category', 'subcategory')
    list_display = ("brand_name", "title","category","subcategory","sell_price","description","active")

@admin.register(productimages)
class productimagesAdmin(admin.ModelAdmin):
    # image_tag = AdminThumbnail(image_field='image')
    # image_tag.short_description = 'Image'
    list_display =("image_tag","product","active","timestamp")
    readonly_fields=[('image_tag')]

    # fields =("image","product","active","timestamp")

@admin.register(category)
class categoryAdmin(admin.ModelAdmin):
    ordering=['title']

@admin.register(subcategory)
class subcategoryAdmin(admin.ModelAdmin):
    ordering=['subcategory_id']
    list_display =("subcategory_id","category","title","timestamp")
    