import uuid

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from .models import *

# Enable or disable email
send_email = False


@login_required
def home(request):
    return redirect('products:product_list')


def login_attempt(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user_obj = User.objects.filter(email=email).first()
        if user_obj is None:
            messages.success(request, 'User not found.')
            return redirect('signup')

        profile_obj = Profile.objects.filter(user=user_obj).first()

        if not profile_obj.is_verified:
            messages.success(request, 'Profile is not verified check your mail.')
            return redirect('signup')

        user = authenticate(username=user_obj.username, password=password)
        if user is None:
            messages.success(request, 'Wrong password.')
            return redirect('signup')

        login(request, user)
        return redirect('products:product_list')

    return render(request, 'signup.html')


def register_attempt(request):
    if request.method == 'POST':
        firstname = request.POST.get('first-name')
        lastname = request.POST.get('last-name')
        email = request.POST.get('email')
        phonenumber = request.POST.get('Number')
        password = request.POST.get('password')

        try:
            if User.objects.filter(email=email).first():
                messages.success(request, 'Email is taken.')
                return redirect('signup')

            user_obj = User(username=email, email=email, first_name=firstname, last_name=lastname)
            user_obj.set_password(password)
            user_obj.save()

            if send_email:
                auth_token = str(uuid.uuid4())
                profile_obj = Profile.objects.create(user=user_obj, auth_token=auth_token)
                profile_obj.save()
                send_mail_after_registration(email, auth_token)
                return redirect('token_send')
            else:
                profile_obj = Profile.objects.create(user=user_obj)
                profile_obj.is_verified = True
                profile_obj.auth_token = ""
                profile_obj.save()
                login(request, user_obj)
                return redirect('products:product_list')

        except Exception as e:
            print(e)
            return redirect("landing_page")

    return render(request, 'signup.html')


def success(request):
    return render(request, 'success.html')


def token_send(request):
    return render(request, 'token_send.html')


def reset_success(request):
    return render(request, 'reset_success.html')


def verify(request, auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token=auth_token).first()

        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request, 'Your account is already verified.')
                return redirect('signup')
            profile_obj.is_verified = True
            profile_obj.auth_token = ""
            profile_obj.save()
            messages.success(request, 'Your account has been verified.')
            return redirect('signup')
        else:
            return redirect('signup')
    except Exception as e:
        print(e)
        return redirect('')


def error_page(request):
    return render(request, 'error.html')


def resetting(request, reset_token):
    try:
        profile_obj = Profile.objects.filter(reset_token=reset_token).first()

        if profile_obj:
            if profile_obj.is_reset:
                messages.success(request, 'You have already used this link to reset your password.')
                return redirect('reset_attempt')
            # profile_obj.is_reset = True
            profile_obj.save()
            messages.success(request, 'You will now be able to reset your password.')
            return redirect('resetpage')
        else:
            return redirect('error')
    except Exception as e:
        print(e)
        return redirect('home')


def send_mail_after_registration(email, token):
    subject = 'Your accounts need to be verified'
    message = f'Hi paste the link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from = 'PricedOut@PricedOut.com'  # settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)


def faq(request):
    return render(request, 'faq.html')


def about_us(request):
    return render(request, 'About.html')


def contact_us(request):
    return render(request, 'Contact.html')


def send_mail_password_reset(email, token):
    subject = 'Reset your password'
    message = f'Hi paste the link to reset your password http://127.0.0.1:8000/resetting/{token}'
    email_from = 'PricedOut@PricedOut.com'  # settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)


def reset_attempt(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        print(email)

        try:
            user = User.objects.filter(email=email).first()
            if user:
                reset_token = str(uuid.uuid4())
                profile_obj = Profile.objects.get(user=user)
                profile_obj.reset_token = reset_token
                profile_obj.save()
                send_mail_password_reset(email, reset_token)
                return redirect('token_send')

            else:
                messages.success(request, 'Email not associated with an account.')
                return redirect('reset_attempt')

        except Exception as e:
            print(e)

    return render(request, 'passwordreset.html')


# user id and the token, check if it is the user id and the correct token


def resetpage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)

        user_obj = User.objects.filter(email=email).first()

        if user_obj is None:
            messages.success(request, 'User not found.')
            return redirect('signup')

        profile_obj = Profile.objects.filter(user=user_obj).first()

        if not profile_obj.is_reset:
            user_obj.set_password(password)
            user_obj.save()
            profile_obj.reset_token = ""
            profile_obj.save()
            return redirect('reset_success')

        if profile_obj.is_reset:
            messages.success(request, 'Please click the link emailed to you with a token.')
            return redirect('resetpage')

    return render(request, 'resetpage.html')


def signup(request):
    return render(request, 'signup.html')


def logout_user(request):
    logout(request)
    return render(request, 'signup.html')


def thank_you(request):
    return render(request, 'thank_you.html')
