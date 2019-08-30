from django.contrib import admin
from .models import Product,ProductImage,Category,Variation
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    search_fields=['title','description']
    list_display = ['title','price','active','updated_date']
    list_filter = ['price','active','updated_date']
    list_editable=['price','active']
    prepopulated_fields={'slug':('title',)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product,ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Variation)
