from django.shortcuts import render, redirect
from goodcauses.models import Signin, Profile, Feedback, Funds, UserProfileInfo
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from goodcauses.forms import UserForm, UserProfileInfoForm
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import send_mail
# from django.contrib.auth.tokens import default_token_generator
# from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator


# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('dash'))
            else:
                return HttpResponse("Account not active")
        else:
            print("Someone with username: {} and password: {} tried to login and failed".format(username,password))
            return HttpResponse("Invalid login Crediantials!")
    else:
        return render(request,"login.html")
    
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('dash'))

def signup(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True

            return HttpResponseRedirect(reverse('dash'))
        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

        # name = request.POST.get("name")
        # username = request.POST.get("username")
        # type = request.POST.get("type")
        # password = request.POST.get("password")
        # ins = Signin(name = name,username = username,type = type,password = password)
        # ins.save()
    return render(request, 'signup.html', {'user_form':user_form, 'profile_form':profile_form, 'registered':registered})

def list(request):
    list = Profile.objects.all()
    name = Signin.objects.all()
    context = {'list' : list, 'name' : name}
    return render(request, 'list.html',context)

def profile(request):
    if request.method == 'POST':
        orgname = request.POST['orgname']
        phone = request.POST["phone"]
        previouswork = request.POST["previouswork"]
        futuregoals = request.POST["futuregoals"]
        fundingneeds = request.POST["fundingneeds"]
        files = request.FILES.get("files")
        ins = Profile(orgname=orgname, phone=phone, previouswork=previouswork, futuregoals=futuregoals,fundingneeds=fundingneeds, files=files)
        ins.save()
    return render(request, 'profile.html')

def fundraising(request):
    if request.method == 'POST':
        frname = request.POST['frname']
        frphone = request.POST["frphone"]
        eventdesc = request.POST["eventdesc"]
        funds = request.POST["funds"]
        documents = request.FILES.get("document")
        ins = Funds(frname=frname, frphone=frphone, eventdesc=eventdesc, funds=funds, documents=documents)
        ins.save()
    return render(request, 'fundraising.html')

def dash(request):
    return render(request, 'dashboard.html')

def feedback(request):
    if request.method == 'POST':
        fname = request.POST.get("fname")
        fusername = request.POST.get("fusername")
        country = request.POST.get("country")
        desc = request.POST.get("desc")
        ins = Feedback(fname = fname,fusername = fusername,country = country,desc = desc)
        ins.save()
    return render(request, 'feedback.html')


token_generator = PasswordResetTokenGenerator()
def forgot_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            associated_users = User.objects.filter(email=email)

            if associated_users.exists():
                for user in associated_users:
                    subject = 'Password Reset Requested'
                    email_template_name = 'forgot_password_email.html'
                    c = {
                        'email': user.email,
                        'domain': 'example.com',
                        'site_name': 'Example',
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'user': user,
                        'token': token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email_message = render_to_string('reset_password.html', c)
                    message = strip_tags(email_message)
                    send_mail(subject, message, 'noreply@example.com', [user.email], html_message=email_message, fail_silently=False)


                messages.success(request, 'Instructions to reset your password have been emailed to you. Please check your email.')
                return redirect('login')
            else:
                messages.error(request, 'No account exists with that email address.')
                return redirect('forgot_password')
    else:
        form = PasswordResetForm()

    return render(request, 'forgot_password.html', {'form': form})


def reset_password(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and token_generator.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                login(request, user)
                messages.success(request, 'Your password has been reset.')
                return redirect('home')
        else:
            form = SetPasswordForm(user)

        return render(request, 'reset_password.html', {'form': form})
    else:
        messages.error(request, 'The password reset link was invalid, possibly because it has already been used. Please request a new password reset.')
        return redirect('login')
