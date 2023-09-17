from django.urls import path
from . import views


urlpatterns = [
    path('Home/', views.home, name='home'),
    path('About/', views.about, name='about'),
    path('Booking/', views.booking, name='booking'),
    path('Menu/', views.menu, name='menu'),
    path('menu_item/<int:pk>/', views.display_menu_items, name='menu_item'),
]
