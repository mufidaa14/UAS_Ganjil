from django.urls import path
from . import views

urlpatterns = [
    path("main/", views.main, name="main"),
    path("jadwal/", views.jadwal, name="jadwal"),
    path("senin/", views.senin, name="senin"),
    path("selasa/", views.selasa, name="selasa"),
    path("kamis/", views.kamis, name="kamis"),
    path("jumat/", views.jumat, name="jumat"),
    path("profil/", views.profil, name="profil"),
    path("contact/", views.contact, name="contact"),
    path("data/", views.data, name="data"),
]