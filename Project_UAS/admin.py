from django.contrib import admin
from.models import absen
from.models import jadwal_hari

class absenAdmin(admin.ModelAdmin):
    list_display = ("hari", "nama", "npm", "fakultas", "prodi",)
    search_fields = ("hari", "nama", "npm", "fakultas", "prodi",)

admin.site.register(absen, absenAdmin)
admin.site.register(jadwal_hari)

# Register your models here.
