# Generated by Django 5.0 on 2023-12-29 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project_UAS', '0003_jadwal_hari_absen_delete_mahasiswa_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='absen',
            name='keterangan',
            field=models.CharField(max_length=20, null=True),
        ),
    ]