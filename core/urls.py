from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('hizmet/<slug:slug>/', views.service_detail, name='service_detail'),
    path('proje/<int:pk>/', views.project_detail, name='project_detail'),
]

