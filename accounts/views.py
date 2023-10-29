from datetime import datetime, time, timezone
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import *
import uuid
from home.utils import *


# Create your views here.


def sign_in(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        passwd = request.POST.get('password')

        userAcc = authenticate(request, email=uname, password=passwd)
        if userAcc is not None:
            if userAcc.email_is_verified == True:  # Must be True
                login(request, userAcc)
                messages.success(request, 'Logged in Successfully')
                return redirect('/')
            else:
                messages.error(request, 'Verified your email ID')
                return redirect('/sign_in')
        # print(userAcc, User.email_is_verified == True)
        print(userAcc)
        messages.error(request, f'{userAcc} Invalid ID and Password')
    return render(request, 'login.html')


def sign_out(request):

    # if request.method == 'GET':
    # User.last_logout_time = datetime

    #     print(str(datetime.now))
    #     if False:
    print(str(User.get_session_auth_hash))
    logout(request)
    messages.warning(request, 'Logout')
    return redirect('/sign_in')


def user_check(request):
    if request.is_authenticated:
        return False
    return True


@ user_passes_test(user_check, login_url='/profile/')
def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user_exists = User.objects.filter(email=email).exists()
        if user_exists:
            messages.error(request, 'Email Address already exist on this site')
            return redirect(register)
        else:
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            passwd = request.POST.get('password')
            clgEmail = request.POST.get('clg_email')
            phNumber = request.POST.get('ph_number')
            gender = request.POST.get('gender')

            if User.objects.filter(clg_email=clgEmail).exists():
                messages.error(request, 'College email already exist')
                return redirect(register)
            else:
                user = User.objects.create_user(
                    first_name=fname, last_name=lname, email=email, password=passwd, clg_email=clgEmail, mobile=phNumber, email_token=str(
                        uuid.uuid4()), gender=gender
                )  # profile_pic=profile_pic)
                if user is not None:
                    print("User Created")
                    send = send_email_token(email, user.email_token)
                    # send = send_mail(
                    #     # Subject
                    #     "testing",
                    #     # Message
                    #     "Verify your account and do not share below link to anyone",
                    #     # from_email
                    #     settings.EMAIL_HOST_USER,
                    #     # to
                    #     [email]
                    # )
                    if send:
                        messages.success(request, "Register Successfully")
                    else:
                        messages.error(request, "Email not send")
                    # return redirect('')
    return render(request, 'register.html')


def verify(request, token):
    try:
        obj = User.objects.get(email_token=token)
        if obj:
            # obj.email_token = None
            obj.email_is_verified = True
            obj.save()
        return HttpResponse('Your Email Address is verified...now you can login')
    except Exception as e:
        return HttpResponse('Invalid Token')
