from django.urls import path

from .views import *


urlpatterns = [
    path('services/', services_list),
    path('services/<int:pk>/', service_page),
    path('create/', create_category)
]
