from django.shortcuts import render, redirect  
from django.http import JsonResponse
from django.contrib import messages  
from .models import Mahasiswa, Berita, Jurusan, KontakPesan  

def beranda(request):
    if request.method == "POST":
        nama = request.POST.get('name')
        email = request.POST.get('email')
        pesan = request.POST.get('message')
        
        if nama and email and pesan:
            KontakPesan.objects.create(nama=nama, email=email, pesan=pesan)
            
            messages.success(request, "Pesan antum berhasil dikirim ke admin!")
            return redirect('beranda') 

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