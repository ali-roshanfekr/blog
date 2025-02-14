from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('error', ErrorView.as_view(), name='error'),
]
