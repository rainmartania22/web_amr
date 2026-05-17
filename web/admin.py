from django.contrib import admin

from import_export import resources, fields
from import_export.admin import ImportExportMixin

from .models import Mahasiswa, Jurusan, Berita

admin.site.register(Jurusan)
admin.site.register(Mahasiswa)
admin.site.register(Berita)
