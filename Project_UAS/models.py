from django.db import models

class absen(models.Model):
  hari = models.CharField(max_length=50)
  makul = models.CharField(max_length=50, null=True)
  nama = models.CharField(max_length=50)
  npm = models.CharField(max_length=50)
  fakultas = models.CharField(max_length=50)
  prodi = models.CharField(max_length=50)
  keterangan = models.CharField(max_length=20, null=True)

  def __str__(self):
    return f"{self.hari}"
  
# Create your models here.
