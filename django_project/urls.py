from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('django_project/', views.django_project, name='django_project'),
    path('django_project/details/<int:id>', views.details, name='details'),
    path('',include('home.urls')),
]
