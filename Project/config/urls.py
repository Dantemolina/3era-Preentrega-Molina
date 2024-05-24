
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacto/', views.contacto, name='contacto'),
    path('termotanques/', views.decoartesanal, name='decoartesanal'),
    path('luminarias/', views.decohogar, name='deco'),
    path('otros_productos/', views.mates, name='mate'),
    path('termotanques/', views.organizadores, name='organizadores'),
    path('luminarias/', views.sobreMi, name='sobreMi'),
]
