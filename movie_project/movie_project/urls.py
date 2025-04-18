from django.contrib import admin
from django.urls import path
from films import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.add_film, name='add_film'),
    path('films/', views.films_list, name='films_list'),
]