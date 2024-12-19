"""
URL configuration for webapp project.

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
from django.urls import path
from practice.views import practice, practice_json
from fhe.views import fhe, fhe_json, fhe_ideas

urlpatterns = [
    path('admin/', admin.site.urls), # here by default
    path('practice/', practice, name='practice'),
    path('practice/json/', practice_json, name='practice_json'),

    path('fhe/', fhe, name='fhe'),
    path('fhe/json/', fhe_json, name='fhe_json'),
    path('fhe/ideas/', fhe_ideas, name='fhe_ideas')
]




# https://webapp.com/practice -- provides a form to be added to the signup list
# https://webapp.com/practice/json -- provides the list of contacts in json format