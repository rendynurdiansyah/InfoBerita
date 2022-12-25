from django.contrib.auth.models import User
from multiprocessing import context
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.shortcuts import render,redirect
from django.http import HttpResponse 
from django.db import  transaction
from django.contrib.auth.hashers import make_password

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from berita.models import Artikel,Berita
from users.models import Biodata
import requests
from django.conf import settings

def index(request):
    template_name = 'front/index.html'
    artikel = Artikel.objects.all()

    page = request.GET.get('page', 1)

    paginator = Paginator(artikel, 3)
    try:
        artikel = paginator.page(page)
    except PageNotAnInteger:
        artikel = paginator.page(1)
    except EmptyPage:
        artikel = paginator.page(paginator.num_pages)

    context = {
        'title':'my home',
        'welcome':'welcome my home',
        'artikel':artikel,
    }
    return render(request, template_name, context)

def detail_artikel(request, id):
    template_name = 'front/detail_artikel.html'
    artikel = Artikel.objects.get(id=id)
    context = {
        'title':'detail',
        'artikel':artikel,
    }
    return render(request, template_name,context)

def blog(request):
    template_name = 'front/blog.html'
    context = {
        'title':'Blog',
        'welcome':'welcome my home',
    }
    return render(request, template_name, context)
def blog(request):
    url = "https://berita-indo-api.vercel.app/v1/cnn-news"

    data = requests.get(url).json()

    a = data['data']
    title = []
    link = []
    konten = []
    date = []
    gambar = []

    for i in range(len(a)):
        f = a[i]
        link.append(f['link'])
        title.append(f['title'])
        konten.append(f['contentSnippet'])
        date.append(f['isoDate'])
        gambar.append(f['image'])

    mylist = zip(title, link,konten,date,gambar)
    context ={'mylist':mylist}

    return render(request, 'front/blog.html', context)

def artikel(request):
    template_name = 'front/artikel.html'
    artikel = Artikel.objects.all()
    context = {
        'title':'Artikel',
        'welcome':'welcome my home',
        'artikel':artikel,
    }
    return render(request, template_name, context)

# def blog(request):
#     template_name = 'front/blog.html'
#     berita = Berita.objects.all()
#     context = {
#         'title':'Berita',
#         'welcome':'welcome my home',
#         'berita':berita,
#     }
#     return render(request, template_name, context)

def about(request):
    template_name = 'front/about.html'
    context = {
        'title':'About Us',
        'welcome':'welcome my home',
    }
    return render(request, template_name, context)

def contact(request):
    template_name = 'front/contact.html'
    context = {
        'title':'Contact Us',
        'welcome':'welcome my home',
    }
    return render(request, template_name, context)    

def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    template_name = 'account/login.html'
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None :
            pass
            print("username benar" )
            auth_login(request, user)
            return redirect('index')
        else:
            pass
            print("username salah" )
    context = {
        'title':'form',
    }
    return render(request, template_name, context)
def logout_view(request):
    logout(request)
    return redirect('index')

def register(request):
    template_name = 'account/register.html'
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        nama_depan = request.POST.get('nama_depan')
        nama_belakang = request.POST.get('nama_belakang')
        email = request.POST.get('email')
        alamat = request.POST.get('alamat')
        telp = request.POST.get('telp')

        try:
            with transaction.atomic():
                User.objects.create(
                    username = username,
                    password = make_password(password),
                    first_name = nama_depan,
                    last_name= nama_belakang,
                    email = email
                )
                get_user = User.objects.get(username = username)
                Biodata.objects.create(
                    user = get_user,
                    alamat = alamat,
                    telp = telp,
                )
            return redirect(index)
        except:pass
        print(username,password,nama_depan,nama_belakang,email,alamat,telp)
    context = {
        'title':'form register',
    }
    return render(request, template_name, context)