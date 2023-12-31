from django.contrib import admin
from.models import absen

class absenAdmin(admin.ModelAdmin):
    list_display = ("hari", "makul","nama", "npm", "fakultas", "prodi",)
    search_fields = ("hari","makul", "nama", "npm", "fakultas", "prodi",)
    list_per_page = 4

admin.site.register(absen, absenAdmin)


# Register your models here.
