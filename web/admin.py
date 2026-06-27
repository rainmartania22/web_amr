from django.contrib import admin
from .models import Mahasiswa, Jurusan, Berita, KontakPesan

# 1. Register Jurusan
admin.site.register(Jurusan)

# 2. Register Mahasiswa (Sekaligus Berfungsi Sebagai Tim)
class MahasiswaAdmin(admin.ModelAdmin):
    # Menampilkan kolom-kolom ini di tabel admin
    list_display = ('no', 'nama', 'nim', 'id_jur', 'match_played', 'win', 'total_poin', 'tim')  # Tambahkan 'tim' ke list_display
    # Membuat kolom poin bisa langsung diedit tanpa harus masuk ke detail satu per satu!
    list_editable = ('match_played', 'win', 'total_poin') 

admin.site.register(Mahasiswa, MahasiswaAdmin)

# 3. Register Berita
admin.site.register(Berita)

# 4. Register Pesan Masuk
admin.site.register(KontakPesan)