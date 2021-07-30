from django.contrib import admin
from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('' ,  home  , name="home"),
    path('register' , views.register_attempt , name="register_attempt"),
    path('login' , views.login_attempt , name="login_attempt"),
    path('token' , token_send , name="token_send"),
    path('reset_success', reset_success, name="reset_success"),
    path('success' , success , name='success'),
    path('verify/<auth_token>' , verify , name="verify"),
    path('error' , error_page , name="error"),
    path('faq' , faq , name="faq"),
    path('resetting/<reset_token>' , resetting , name="resetting"),
    path('passwordreset' , reset_attempt , name="reset_attempt"),
    path('resetpage' , resetpage , name="resetpage"),
    path('signup/' , views.signup, name="signup"),
   
]