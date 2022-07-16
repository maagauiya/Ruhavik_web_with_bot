
from django.urls import path, include

from .views import *


urlpatterns = [
  path('main/',main,name='main'),
  path('test/',test,name='test'),
  path('start/',start,name='start'),
  path('kms/',kms,name='kms'),
]   