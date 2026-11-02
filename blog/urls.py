from django.urls import path
from . import views
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('post/<int:pk>/', views.detalle_post, name='detalle_post'),
    path('post/crear/', views.crear_post, name='crear_post'),
    path('post/<int:pk>/editar/', views.editar_post, name='editar_post'),
    path ('post/<int:pk>/eliminar/', views.eliminar_post, name='eliminar_post'),
    path ('registro/', views.registro, name='registro'),
    path ('login/', views.login_usuario, name='login'),
    path ('logout/', views.logout_usuario, name='logout'),
    
]