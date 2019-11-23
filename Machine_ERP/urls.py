"""Machine_ERP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from djgeojson.views import GeoJSONLayerView
from ERP.views import index
from ERP.views import mainpage
from ERP.views import register
from ERP.views import map
from ERP.views import databases
from ERP.views import logout
from ERP.views import notes
from ERP.views import chart
from ERP.views import speech
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('mainpage/', mainpage),
    path('register/', register),
    path('map/', map),
    path('databases/', databases),
   path('logout/', logout),
    path('note/', notes),
    path('chart/', chart),
    path('speech/', speech),


]

