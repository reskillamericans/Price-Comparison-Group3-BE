from django.urls import path

from . import views
from .views import *

urlpatterns = [
    # path('', home, name="home"),
    path('register', views.register_attempt, name="register_attempt"),
    path('login', views.login_attempt, name="login_attempt"),
    path('logout', logout_user, name="logout"),
    path('token', token_send, name="token_send"),
    path('reset_success', reset_success, name="reset_success"),
    path('success', success, name='success'),
    path('verify/<auth_token>', verify, name="verify"),
    path('error', error_page, name="error"),
    path('faq', faq, name="faq"),
    path('about_us', about_us, name="about_us"),
    path('contact_us', contact_us, name="contact_us"),
    path('resetting/<reset_token>', resetting, name="resetting"),
    path('passwordreset', reset_attempt, name="reset_attempt"),
    path('resetpage', resetpage, name="resetpage"),
    path('signup/', views.signup, name="signup"),
    path('thank_you/', views.thank_you, name="thank_you"),
    ]
