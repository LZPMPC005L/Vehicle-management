"""
URL configuration for django11 project.

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
from vehicle.views import PlateRegistration, IdentfitionRecord, UserRegistration,Violation,AreaCondition,jump_years,jump_years1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('plate/', PlateRegistration.as_view()),
    path('user/', UserRegistration.as_view()),
    path('record/', IdentfitionRecord.as_view()),
    path('violation/', Violation.as_view()),
    path('areacondition/',AreaCondition.as_view(),name='areacondition'),
    path('areacondition/show_years/', jump_years, name="show_years"),
    path('areacondition/show_years1/', jump_years1, name="show_years1")
]
