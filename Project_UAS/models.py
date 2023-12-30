from django.db import models

class jadwal_hari(models.Model):
  makul = models.CharField(max_length=50)

  def __str__(self):
    return f"{self.makul}"
  
class absen(models.Model):
  hari = models.ForeignKey(jadwal_hari, on_delete=models.CASCADE)
  nama = models.CharField(max_length=50)
  npm = models.CharField(max_length=50)
  fakultas = models.CharField(max_length=50)
  prodi = models.CharField(max_length=50)
  keterangan = models.CharField(max_length=20, null=True)

  def __str__(self):
    return f"{self.nama}"
  
# Create your models here.
