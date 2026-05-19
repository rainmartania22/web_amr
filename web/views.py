from django.shortcuts import render
from django.http import JsonResponse
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

def mahasiswa_json(request):
    # Mengambil semua data mahasiswa dari database
    mahasiswa_list = Mahasiswa.objects.all()
    
    data = []
    for index, mhs in enumerate(mahasiswa_list, start=1):
        data.append({
            'no': index,
            'nim': mhs.nim,
            'nama': mhs.nama,
            'email': mhs.email,
            'id_jur': mhs.id_jur.nama if mhs.id_jur else '-'  # Menampilkan nama jurusan
        })
        
    # Mengembalikan data dalam format JSON yang dimengerti DataTables
    return JsonResponse({'data': data})