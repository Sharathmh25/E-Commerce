from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('Collections/', views.Collections, name='Collections'),
    path('cart/', views.cart, name='cart'),
    path('trendings/', views.trendings, name='trendings'),
    path('Account/', views.Account, name='Account'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('Completetransaction/', views.Completetransaction, name='Completetransaction'),
]