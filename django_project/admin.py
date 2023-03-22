from django.contrib import admin
from .models import Name

class NameAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "phone",)

admin.site.register(Name, NameAdmin)
