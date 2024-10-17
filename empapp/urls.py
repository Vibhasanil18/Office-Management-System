"""
URL configuration for officeempmanage project.

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

from django.urls import path
from empapp import views

urlpatterns = [
    path('index',views.index,name='index'),
    path('allemp',views.allemp,name='allemp'),
    path('addemp',views.addemp,name='addemp'),
    path('removeemp',views.removeemp,name='removeemp'),
    path('removeemp/<int:emp_id>',views.removeemp,name='removeemp'),
    path('filteremp',views.filteremp,name='filteremp'),
    

   
]
