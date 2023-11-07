from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name ='home'),
    path('create/', createShortURL, name='create'),
    path('list_all_urls/', list_all_urls, name ="list_all_urls")
]