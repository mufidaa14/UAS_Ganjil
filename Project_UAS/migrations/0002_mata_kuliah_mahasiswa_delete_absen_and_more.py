# Generated by Django 5.0 on 2023-12-29 03:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project_UAS', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mata_kuliah',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hari', models.CharField(max_length=255)),
                ('makul', models.CharField(max_length=255)),
                ('jumlah_sks', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Mahasiswa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('NPM', models.CharField(max_length=255)),
                ('Prodi', models.CharField(max_length=255)),
                ('Mata_kuliah', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Project_UAS.mata_kuliah')),
            ],
        ),
        migrations.DeleteModel(
            name='absen',
        ),
        migrations.DeleteModel(
            name='jadwal_hari',
        ),
    ]