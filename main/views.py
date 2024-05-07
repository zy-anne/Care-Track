from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from .models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_screen_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Attempt to authenticate the user
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            if user.is_active:
                # If the user is active, log them in
                login(request, User)
                # Redirect to a success page
                return redirect('/main-menu/')
            else:
                # User account is disabled
                messages.error(request, 'Your account is disabled.')
        else:
            # Authentication failed
            messages.error(request, 'Invalid email or password.')
    
    # If the request method is GET or authentication failed, render the login page
    return render(request, 'login.html')

def signup_screen_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('/main-menu/')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def home_screen_view(request):
    return render(request, 'home.html')

def about_screen_view(request):
    return render(request, 'about.html')

def billing_screen_view(request):
    return render(request, 'billing.html')

def feedback_screen_view(request):
    return render(request, 'feedback.html')

def index_screen_view(request):
    return render(request, 'index.html')

def main_menu_screen_view(request):
    return render(request, 'main-menu.html')

def results_screen_view(request):
    return render(request, 'results.html')

def healthinfo_screen_view(request):
    return render(request, 'health-information.html')

def assessment_screen_view(request):
    return render(request, 'health-assessment.html')

def gensurvey_screen_view(request):
    return render(request, 'general-survey.html')

def integumentary_screen_view(request):
    return render(request, 'integumentary-system.html')

def musculoskeletal_screen_view(request):
    return render(request, 'musculoskeletal-system.html')

def vitalsigns_screen_view(request):
    return render(request, 'vital-signs.html')

def history_screen_view(request):
    return render(request, 'medical-history.html')

