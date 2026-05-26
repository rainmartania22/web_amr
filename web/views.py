from django.shortcuts import render
from django.http import JsonResponse
from .models import Mahasiswa, Berita, Jurusan

def beranda(request):
    berita_list = Berita.objects.all().order_by('-tanggal_dibuat')
    
    context = {
        'berita_list': berita_list
    }
    
    return render(request, 'index.html', context)

def mahasiswa_json(request):
    mahasiswa_list = Mahasiswa.objects.all()
    
    data = []
    for index, mhs in enumerate(mahasiswa_list, start=1):
        data.append({
            'no': index,
            'nim': mhs.nim,
            'nama': mhs.nama,
            'email': mhs.email,
            'id_jur': mhs.id_jur.nama if mhs.id_jur else '-'  
        })
        
    return JsonResponse({'data': data})