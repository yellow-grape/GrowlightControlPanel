from django.urls import path,include
from .views import *
urlpatterns = [
   path('',homepage),
   path('change',change),
]
   