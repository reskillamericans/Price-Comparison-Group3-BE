from accounts.models import Profile
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
    return render(request , 'home.html')



def login_attempt(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user_obj = User.objects.filter(email = email).first()
        if user_obj is None:
            messages.success(request, 'User not found.')
            return redirect('/login')
        
        
        profile_obj = Profile.objects.filter(user = user_obj ).first()

        if not profile_obj.is_verified:
            messages.success(request, 'Profile is not verified check your mail.')
            return redirect('/login')

        user = authenticate(email = email , password = password)
        if user is None:
            messages.success(request, 'Wrong password.')
            return redirect('/login')
        
        login(request , user)
        return redirect('/')

    return render(request , 'login.html')

def register_attempt(request):

    if request.method == 'POST':
        firstName = request.POST.get('firstname')
        lastName = request.POST.get('lastname')
        email = request.POST.get('email')
        phoneNumber = request.POST.get('number')
        password = request.POST.get('password')
        print(password)

        try:

            if User.objects.filter(email = email).first():
                messages.success(request, 'Email is taken.')
                return redirect('/register')
            
            user_obj = User(email = email , firstname = firstname , lastname = lastname , number = number)
            user_obj.set_password(password)
            user_obj.save()
            auth_token = str(uuid.uuid4())
            profile_obj = Profile.objects.create(user = user_obj , auth_token = auth_token)
            profile_obj.save()
            send_mail_after_registration(email , auth_token)
            return redirect('/token')

        except Exception as e:
            print(e)
            return redirect("/")


    return render(request , 'register.html')

def success(request):
    return render(request , 'success.html')


def token_send(request):
    return render(request , 'token_send.html')

def resetpage(request):
    return render(request , 'resetpage.html')

def reset_success(request):
    return render(request , 'reset_success.html')



def verify(request , auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token = auth_token).first()
    

        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request, 'Your account is already verified.')
                return redirect('/login')
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, 'Your account has been verified.')
            return redirect('/login')
        else:
            return redirect('/error')
    except Exception as e:
        print(e)
        return redirect('/')

def error_page(request):
    return  render(request , 'error.html')

def resetting(request , reset_token):
    try:
        profile_obj = Profile.objects.filter(reset_token = reset_token).first()
    

        if profile_obj:
            if profile_obj.is_reset:
                messages.success(request, 'You have already used this link to reset your password.')
                return redirect('/passwordreset')
            profile_obj.is_reset = True
            profile_obj.save()
            messages.success(request, 'You will now be able to reset your password.')
            return redirect('/resetpage')
        else:
            return redirect('/error')
    except Exception as e:
        print(e)
        return redirect('/')


def error_page(request):
    return  render(request , 'error.html')






def send_mail_after_registration(email , token):
    subject = 'Your accounts need to be verified'
    message = f'Hi paste the link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list )


def send_mail_password_reset(email , token):
    subject = 'Reset your password'
    message = f'Hi paste the link to reset your password http://127.0.0.1:8000/resetting/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list )




def reset_attempt(request):
 
    if request.method == 'POST':
        email = request.POST.get('email')
        print(email)

        try:

            if User.objects.filter(email = email).first():
                reset_token = str(uuid.uuid4())
                profile_obj = Profile.objects.create(reset_token = reset_token)
                profile_obj.save()
                send_mail_password_reset(email , reset_token)
                return redirect('/token')
            
            else:
                messages.success(request, 'Email not associated with an account.')
                return redirect('/passwordreset')

        except Exception as e:
            print(e)
    
    return render(request , 'passwordreset.html')

# user id and the token, check if it is the user id and the correct token




def resetpage(request):
 
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(password)

        
        user_obj = User.objects.filter(email = email).first()
        
        if user_obj is None:
            messages.success(request, 'User not found.')
            return redirect('/login')
        
        profile_obj = Profile.objects.filter(user = user_obj).first()

        if not profile_obj.is_reset:
            user_obj.set_password(password)
            user_obj.save()
            return redirect('/reset_success')
        
        if profile_obj.is_reset:
            messages.success(request, 'Please click the link emailed to you with a token.')
            return redirect('/resetpage')
    
    return render(request , 'resetpage.html')


def signup(request):
    return render(request, 'signup.html')