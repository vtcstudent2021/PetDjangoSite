from django.urls import path
from petapp import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('serivce/', views.serivce, name='serivce'),
    path('news/', views.news, name='news'),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]