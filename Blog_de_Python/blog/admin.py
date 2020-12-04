from django.contrib import admin
from .models import Category, Article



class CategoryAdmin(admin.ModelAdmin):
    pass



# Register your models here.

admin.site.register(Category)
admin.site.register(Article)
