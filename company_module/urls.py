from django.urls import path
from .views import *

urlpatterns = [
    path('', CompanyView.as_view(), name='company'),
    path('fw/', CompanyFWView.as_view(), name='company_fw'),
    path('details/<id>/', CompanyDetailsView.as_view(), name='company_details'),
]
