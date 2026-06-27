from datetime import datetime
from django.db import models
from django.utils import timezone

class Jurusan(models.Model):
    no = models.AutoField(auto_created=True, primary_key=True, serialize=True)
    nama = models.CharField(max_length=100, blank=False, null=False)
    def __str__(self):
        return self.nama
    class Meta:
        verbose_name_plural = "Jurusan"

class Mahasiswa(models.Model):
    no = models.AutoField(auto_created=True, primary_key=True, serialize=True)
    nama = models.CharField(max_length=100, blank=False, null=False)
    handphone = models.CharField(max_length=13, default="", blank=False, null=False)
    email = models.EmailField(max_length=50, blank=False, null=False)
    nim = models.CharField(max_length=12, blank=False, null=False)
    id_jur = models.ForeignKey(Jurusan, on_delete=models.SET_NULL, null=True)
    timestamp = models.TimeField(default=timezone.now, null=True, blank=True)
    tim = models.CharField(max_length=100, blank=True, null=True)  # Tambahkan field tim
    
    # 3 FIELD INI WAJIB ADA BIAR KLASEMEN TIDAK ERROR
    match_played = models.IntegerField(default=0)
    win = models.IntegerField(default=0)
    total_poin = models.IntegerField(default=0)
    
    def __str__(self):
        return self.nama
    class Meta:
        verbose_name_plural = "Mahasiswa"       

class Berita(models.Model):
    judul = models.CharField(max_length=200)
    isi = models.TextField()
    gambar = models.ImageField(upload_to='berita_images/', blank=True, null=True)
    tanggal_dibuat = models.DateTimeField(default=timezone.now, verbose_name="Tanggal Rilis Berita")

    def __str__(self):
        return self.judul
        
    class Meta:
        verbose_name_plural = "Berita"

class KontakPesan(models.Model):
    nama = models.CharField(max_length=100)
    email = models.EmailField()
    pesan = models.TextField()
    tanggal_kirim = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pesan dari {self.nama} ({self.email})"

    class Meta:
        verbose_name_plural = "Daftar Pesan Masuk"