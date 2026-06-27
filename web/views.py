from django.shortcuts import render, redirect  
from django.http import JsonResponse
from django.contrib import messages  
from django.db.models import Sum
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import Mahasiswa, Berita, Jurusan, KontakPesan

def beranda(request):
    if request.method == "POST":
        nama = request.POST.get('name')
        email = request.POST.get('email')
        pesan = request.POST.get('message')
        
        if nama and email and pesan:
            KontakPesan.objects.create(nama=nama, email=email, pesan=pesan)
            messages.success(request, "Pesan anda berhasil dikirim ke admin!")
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
    # INI TAMBAHAN RETURN YANG SEMPAT HILANG
    return JsonResponse({'data': data})

def klasemen_datatable(request):
    # Urutkan berdasarkan total_poin tertinggi
    data_mhs = Mahasiswa.objects.all().order_by('-total_poin')
    
    data_klasemen = []
    for index, mhs in enumerate(data_mhs, start=1):
        
        # LOGIKA BARU: Jika belum pernah main (match_played == 0), maka rank disamarkan jadi "-"
        if mhs.match_played == 0:
            rank_tampil = "-"
        else:
            rank_tampil = index

        data_klasemen.append({
            "rank": rank_tampil,         # <--- Ganti 'index' dengan 'rank_tampil'
            "nim": mhs.nim,
            
            # (Pastikan mapping data di bawah ini sama persis dengan yang antum punya sebelumnya)
            "nama_tim": mhs.tim,       
            "nama_kapten": mhs.nama,     
            "jurusan": mhs.id_jur.nama if mhs.id_jur else "-", 
            "match_played": mhs.match_played,
            "win": mhs.win,
            "total_poin": mhs.total_poin
        })
        
    return JsonResponse({"data": data_klasemen})

def gabung_komunitas(request):
    if request.method == 'POST':
        email_input = request.POST.get('email_komunitas')
        
        KontakPesan.objects.create(
            nama="Member Komunitas Baru",
            email=email_input,
            pesan="Request bergabung ke dalam info turnamen & komunitas E-Sports."
        )
        
        messages.success(request, f"Selamat! Email {email_input} berhasil terdaftar dalam komunitas kami. 🚀")
        
    return redirect('/#home')

def daftar_tim(request):
    if request.method == 'POST':
        nama_input = request.POST.get('nama')
        hp_input = request.POST.get('handphone')
        email_input = request.POST.get('email')
        nim_input = request.POST.get('nim')
        tim_input = request.POST.get('tim')
        jurusan_no = request.POST.get('jurusan') # Mengambil nomor PK jurusan dari form

        try:
            # Cari jurusan berdasarkan kolom 'no'
            jurusan_obj = Jurusan.objects.get(no=jurusan_no)

            # Simpan data
            Mahasiswa.objects.create(
                nama=nama_input,
                handphone=hp_input,
                email=email_input,
                nim=nim_input,
                tim=tim_input,
                id_jur=jurusan_obj
            )
            
            messages.success(request, f'Tim {tim_input} berhasil didaftarkan!')
            return redirect('/') # Sesuaikan dengan nama route halaman utama di urls.py
            
        except Exception as e:
            messages.error(request, f'Gagal mendaftar: {str(e)}')

    # Lempar data jurusan ke HTML untuk dropdown
    daftar_jurusan = Jurusan.objects.all()
    return render(request, 'daftar_tim.html', {'daftar_jurusan': daftar_jurusan})

def cek_jadwal(request):
    # 1. Otomatis hitung total tim terdaftar dari model Mahasiswa
    total_tim = Mahasiswa.objects.count() 
    
    # 2. Otomatis hitung total match yang sudah berjalan berdasarkan data klasemen
    total_match_berjalan = Mahasiswa.objects.aggregate(Sum('match_played'))['match_played__sum'] or 0
    total_match = int(total_match_berjalan / 2)
    
    # 3. Data List Jadwal Pertandingan Antum
    jadwal_match = [
        {
            "waktu": "HARI INI - 19:00 WIB",
            "tim_kiri": "SLEK-ESPORT",
            "tim_kanan": "INFEST",
            "status": "live"
        },
        {
            "waktu": "HARI INI - 20:30 WIB",
            "tim_kiri": "SHADES",
            "tim_kanan": "MORVEX2",
            "status": "upcoming"
        },
        {
            "waktu": "BESOK - 15:00 WIB",
            "tim_kiri": "GANASH",
            "tim_kanan": "BZZT",
            "status": "upcoming"
        },
        {
            "waktu": "BESOK - 15:00 WIB",
            "tim_kiri": "COLOR_IJO",
            "tim_kanan": "RAJA KNOCK",
            "status": "upcoming"
        }
    ]
    
    # 4. Kirim semua data ke file HTML
    context = {
        'jadwal_match': jadwal_match,
        'total_tim': total_tim,
        'total_match': total_match,
    }
    return render(request, 'cek_jadwal.html', context)

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Langsung login otomatis setelah daftar
            messages.success(request, f"Akun berhasil dibuat! Selamat datang, {user.username}.")
            return redirect('beranda')
    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Berhasil login. Selamat datang kembali, {user.username}!")
            return redirect('beranda')
    else:
        form = AuthenticationForm()
        
    return render(request, 'login.html', {'form': form})

def logout_user(request):
    logout(request)
    messages.success(request, "Anda telah berhasil logout.")
    return redirect('beranda')