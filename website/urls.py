from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('contact.html', views.contact, name = 'contact'),
    path('about/', views.about, name = 'about'),
    path('service/', views.service, name = 'service'),
    path('pricing/', views.pricing, name = 'pricing'),
    path('success/', views.success, name='success'),
]
