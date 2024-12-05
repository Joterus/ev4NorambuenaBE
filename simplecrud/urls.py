"""
URL configuration for simplecrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from proyects import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/projects/', views.vista_proyecto, name="vista_proyecto"),
    path('', include('proyects.urls')),
    path('delete/<int:project_id>/',
         views.eliminar_proyecto, name="eliminar_proyecto"),
    path('update/<int:project_id>/', views.actualizar_proyecto,
         name="actualizar_proyecto"),


]
