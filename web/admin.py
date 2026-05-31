from django.contrib import admin

from import_export import resources, fields
from import_export.admin import ImportExportMixin

from .models import Mahasiswa, Jurusan, Berita, KontakPesan

admin.site.register(Jurusan)
admin.site.register(Mahasiswa)
admin.site.register(Berita)
class KontakPesanAdmin(admin.ModelAdmin):
    list_display = ('nama', 'email', 'tanggal_kirim', 'pesan')
    search_fields = ('nama', 'email', 'pesan')
    list_filter = ('tanggal_kirim',)
    readonly_fields = ('tanggal_kirim',) 

admin.site.register(KontakPesan, KontakPesanAdmin)