#import views
from app_main import views as main_views

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('',main_views.main_home),
    path('about/',main_views.main_about),
    path('contact/',main_views.main_contact)

]