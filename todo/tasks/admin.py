from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Task),
admin.site.register(Language),
admin.site.register(UAWebiste),

# class LanguagesInline(admin.StackedInline):
#     model = Languages

# class LanguageAdmin(admin.ModelAdmin):
#     inlines = [
#         LanguagesInline,
#     ]