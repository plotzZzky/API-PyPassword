from django.urls import path

from . import views


urlpatterns = [
    path('', views.open_db, name='open_db'),
    path('add/', views.update_password, name='add_pwd'),
    path('del/', views.del_password, name='del_pwd'),
    path('new/', views.generate_password, name='generate'),
    path('download/', views.download, name='download'),
]
