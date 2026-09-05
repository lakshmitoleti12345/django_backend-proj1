"""
URL configuration for first_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.urls import path
from first_project import views
from myapp import views as mypage
from myapp2 import views as views2


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.homepage,name='home'),
    path('jsonpage/',views.jsonpage,name='jsonpage'),
    path('service/',views.service,name='service'),
    path('demopage/', views.demopage),
    path('homepage/',views.homepage),
    path('login/',views.login),
    path('profile/',views.ProfilePage),
    path('myapp_page/',mypage.pages),
     path('myapp_page2/',views2.app2),
     path('products/',views.getproducts),
     path('students/',views.get_students)
]
