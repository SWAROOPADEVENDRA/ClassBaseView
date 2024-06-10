"""
URL configuration for ClassBaseView project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),

    #url patterns for string response by using FBV and CBV
    path('stirngByFbv/',stirngByFbv,name='stirngByFbv'),
    path('StringByCbv/',StringByCbv.as_view(),name='StringByCbv'),

    # URL patterns for HTML response by using FBV and CBV
    path('htmlByFbv/',htmlByFbv,name='htmlByFbv'),
    path('HtmlByCbv/',HtmlByCbv.as_view(),name='HtmlByCbv')

]
