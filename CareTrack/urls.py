"""

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from main.views import (
    home_screen_view,
    about_screen_view,
    billing_screen_view,
    feedback_screen_view,
    index_screen_view,
    results_screen_view,
    login_screen_view,
    signup_screen_view,
    main_menu_screen_view,
    healthinfo_screen_view,
    assessment_screen_view,
    gensurvey_screen_view,
    integumentary_screen_view,
    musculoskeletal_screen_view,
    vitalsigns_screen_view,
    history_screen_view
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', home_screen_view, name="index"),
    path ('about/', about_screen_view, name="about"),
    path ('billing/', billing_screen_view, name="billing"),
    path ('feedback/', feedback_screen_view, name="feedback"),
    path ('index/', index_screen_view, name="index"),
    path ('login/', login_screen_view, name="login"),
    path ('signup/', signup_screen_view, name="signup"),
    path ('main-menu/', main_menu_screen_view, name="main-menu"),
    path ('results/', results_screen_view, name="results"),
    path ('health-information/', healthinfo_screen_view, name="health-information"),
    path ('health-assessment/', assessment_screen_view, name="health-assessment"),
    path ('health-assessment/general-survey/', gensurvey_screen_view, name="general-survey"),
    path ('health-assessment/integumentary-system/', integumentary_screen_view, name="integumentary-system"),
    path ('health-assessment/musculoskeletal-system/', musculoskeletal_screen_view, name="musculoskeletal-system"),
    path ('vital-signs/', vitalsigns_screen_view, name="vital-signs"),
    path ('medical-history/', history_screen_view, name="medical-history")
    
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
