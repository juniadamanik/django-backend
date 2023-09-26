from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # ex: /pools/5/
    path("<int:question_id>/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("<int : question_id/results/, views.vote, name="vote"),

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django,urls import reverse
from django.contrib import admin
from django.urls import path, include
from perpustakaan.views import *
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from perpustakaan.viewset_api import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('kelompok/', KelompokViewset)

urlpatterns = [
    path('api/', include())
    path('',home, name='home'),
    path('admin/', admin.site.urls),
    path('penerbit/', penerbit, name='penerbit'),
    path('buku/', buku, name='buku'),
    path('buku/tambah/', tambah_buku, name='tambah_buku'),
    path('buku/ubah/<int:id_buku>', ubah_buku, name='ubah_buku'),
    path('buku/hapus/<int:id_buku>', hapus_buku, name="hapus_buku"),
    path('buku/export/xls/', export_xls, name='export_xls'),
    path('auth/masuk/', LoginView.as_view(), name='masuk'),
    path('auth/keluar', LogoutView.as view(next_name='masuk'), name='keluar')
]