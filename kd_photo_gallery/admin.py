from django.contrib import admin
from .models import Location,Image,category

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal =('category',)

# Register your models here.
admin.site.register(Location)
admin.site.register(Image,ImageAdmin)
admin.site.register(category)
