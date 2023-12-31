from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import absen
from .forms import Formabsen
from django.contrib import messages


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

def ubah_data(request, id_data):
    data = absen.objects.get(id=id_data)
    template = 'ubah_data.html'
    if request.POST:
        form = Formabsen(request.POST,instance=data)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil diperbarui")
            return redirect('ubah_data', id_data=id_data)
    else:
        form = Formabsen(instance=data)
        context = {
            'form':form,
            'data':data,
        }
    return render(request, template, context)
def data(request):    
    datas = absen.objects.all().values()[:5]
    layout = loader.get_template('data.html') 
    context = {
        'datas': datas
    }
    return HttpResponse(layout.render(context))

def menambah(request):
    if request.POST:
        form = Formabsen(request.POST)
        if form.is_valid():
            form.save()
            form = Formabsen()
            pesan = "Data berhasil disimpan"

            context = {
                'form':form,
                'pesan':pesan,
            }
            return render (request, 'menambah.html', context)
    else :
        form = Formabsen()

        context = {
            'form':form,
    }
    return render(request, 'menambah.html', context)