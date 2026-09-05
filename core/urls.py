from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
   path('about/', views.about, name='about'),
   path('galeria/', views.galeria, name='galeria'),
    
    # Dashboard CRUD
    path('panel/', views.dashboard, name='dashboard'),
    path('panel/nueva/', views.crear_foto, name='crear_foto'),
    path('panel/editar/<int:pk>/', views.editar_foto, name='editar_foto'),
    path('panel/eliminar/<int:pk>/', views.eliminar_foto, name='eliminar_foto'),
    
    # Autenticación
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('panel/categoria/nueva/', views.crear_categoria, name='crear_categoria'),
    path('panel/categoria/eliminar/<int:pk>/', views.eliminar_categoria, name='eliminar_categoria'),
]