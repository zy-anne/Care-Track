from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

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

def login_screen_view(request):
    return render(request, 'login.html')

def main_menu_screen_view(request):
    return render(request, 'main-menu.html')

def results_screen_view(request):
    return render(request, 'results.html')
