from django.shortcuts import render
from ajax_datatable.views import AjaxDatatableView
from .models import Mahasiswa, Berita, Jurusan

def beranda(request):
    # Mengambil semua data berita, diurutkan dari yang terbaru
    berita_list = Berita.objects.all().order_by('-tanggal_dibuat')
    
    # Memasukkan data ke dalam dictionary 'context'
    context = {
        'berita_list': berita_list
    }
    
    # Mengirim context ke template
    return render(request, 'index.html', context)

class MahasiswaAjaxDatatableView(AjaxDatatableView):
    model = Mahasiswa
    title = 'Daftar Mahasiswa'
    initial_order = [["no", "asc"], ] 
    length_menu = [[10, 20, 50, 100], [10, 20, 50, 100]]

    column_defs = [
        # 'name' harus sesuai dengan variabel di models.py kamu
        {'name': 'no', 'title': 'NO', 'visible': True}, 
        {'name': 'nim', 'title': 'NIM', 'visible': True},
        {'name': 'nama', 'title': 'NAMA', 'visible': True},
        {'name': 'email', 'title': 'EMAIL', 'visible': True},
        # Menggunakan 'id_jur' karena itu nama ForeignKey di model Mahasiswa kamu
        {'name': 'id_jur', 'foreign_field': 'id_jur__nama', 'title': 'JURUSAN'}
    ]