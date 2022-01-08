from django.contrib import admin
from . import models
from . models import User
# Register your models here.

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'id',]

@admin.register(models.Detail_Category)
class Detail_CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'detail_name', 'image',]

@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['review', 'time', 'good_teach', 'kind', 'user',]
    
admin.site.register(User)