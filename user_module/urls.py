from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LogInView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('activation/', ActivationView.as_view(), name='activation'),
    path('forget_pass/', ForgetPasswordView.as_view(), name='forget_pass'),
    path('forget_pass_activation/', ForgetPassActivationView.as_view(), name='forget_pass_activation'),
    path('logout/', log_out, name='logout'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile_activation/', ProfileActivationView.as_view(), name='profile_activation'),
    path('new_code/', NewCodeView.as_view(), name='new_code'),
]
