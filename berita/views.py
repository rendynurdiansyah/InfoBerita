from re import template
import re
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render,redirect
from multiprocessing import context
from .models import Artikel, Kategori, Berita
from django.contrib.auth.models import User
from django.conf import settings
from .forms import Artikelforms
import requests



def is_operator(user):
    if user.groups.filter(name='Operator').exists():
        return True
    else :
        return False

@login_required
def dashboard(request):
    if request.user.groups.filter(name='Operator').exists():
        request.session['is_operator'] = 'operator'
        
    template_name = "back/dashboard.html"
    context = {
        'title' : 'dashboard',
    } 
    return render(request, template_name, context)

@login_required
def artikel(request):
    template_name = "back/tabel_artikel.html"
    artikel = Artikel.objects.filter(nama = request.user)
    context = {
        'title' : 'Tabel Artikel',
        'artikel': artikel,
    }
    return render(request, template_name, context)

@login_required
def berita(request):
    template_name = "back/tabel_berita.html"
    berita = Berita.objects.all()
    context = {
        'title' : 'Tabel Berita',
        'berita': berita,
    }
    return render(request, template_name, context)

@login_required
def tambah_artikel(request):
    template_name = "back/tambah_berita.html"
    kategori = Kategori.objects.all()
    if request.method == "POST":
        forms_artikel = Artikelforms(request.POST)
        if forms_artikel.is_valid():
            art = forms_artikel.save(commit=False)
            art.nama = request.user
            art.save()
        return redirect (artikel)
    else :
        forms_artikel = Artikelforms()
    context = {
        'title':'Tambah Artikel',
        'kategori':kategori,
        'forms_artikel' : forms_artikel

    }
    return render(request, template_name, context)

@login_required
def lihat_artikel(request, id):
    template_name = "back/lihat_artikel.html"
    artikel = Artikel.objects.get(id=id)
    context = {
        'title' : 'View Berita',
        'artikel' :artikel,
    }
    return render(request, template_name, context)

@login_required
def edit_artikel(request ,id ):
    template_name = 'back/tambah_berita.html'
    kategori = Kategori.objects.all()
    a = Artikel.objects.get(id=id)
    if request.method == "POST":
        forms_artikel = Artikelforms(request.POST, instance=a)
        if forms_artikel.is_valid():
            art = forms_artikel.save(commit=False)
            art.nama = request.user
            art.save()
        return redirect (artikel)
    else :
        forms_artikel = Artikelforms(instance=a)
        
    context = {
        'title':'Edit Artikel',
        'kategori':kategori,
        'artikel' : artikel,
        'forms_artikel':forms_artikel
    }
    return render(request, template_name, context)

@login_required
def delete_artikel(request,id):
    Artikel.objects.get(id=id).delete()
    return redirect(artikel)

@login_required
@user_passes_test(is_operator)
def users(request):
    template_name = "back/tabel_users.html"
    list_user = User.objects.all()
    context = {
        'title' :'Tabel User',
        'list_user' : list_user
    }
    return render(request, template_name, context)

def sinkron_berita(request):
	url = "https://berita-indo-api.vercel.app/v1/cnn-news"
	data = requests.get(url).json()
	for d in data['data']:
		cek_berita = Berita.objects.filter(title=d['title'])
		if cek_berita:
			print('data sudah ada')
			c = cek_berita.first()
			c.title=d['title']
			c.save()
		else: 
      		#jika belum ada maka tulis baru kedatabase
			b = Berita.objects.create(
				title = d['title'],
				link = d['link'],
				konten = d['contentSnippet'],
				date = d['isoDate'],
				gambar = d['image'],
			
			)
	return redirect(berita)
