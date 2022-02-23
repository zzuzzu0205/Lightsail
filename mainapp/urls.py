from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

appname = 'mainapp'

urlpatterns = [

    path('', TemplateView.as_view(template_name="mainapp/left_bar.html"), name='main'),

]
