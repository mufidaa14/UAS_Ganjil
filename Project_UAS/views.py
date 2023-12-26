from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())
def jadwal(request):
    template = loader.get_template('jadwal.html')
    return HttpResponse(template.render())
def senin(request):
    template = loader.get_template('senin.html')
    return HttpResponse(template.render())
def selasa(request):
    template = loader.get_template('selasa.html')
    return HttpResponse(template.render())
def kamis(request):
    template = loader.get_template('kamis.html')
    return HttpResponse(template.render())
def jumat(request):
    template = loader.get_template('jumat.html')
    return HttpResponse(template.render())
def profil(request):
    template = loader.get_template('profil.html')
    return HttpResponse(template.render())
def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())