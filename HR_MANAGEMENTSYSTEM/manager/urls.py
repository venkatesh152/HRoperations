"""HR_MANAGEMENTSYSTEM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.views.generic import TemplateView
from django import views

from manager import views

urlpatterns = [

    path('manager/',TemplateView.as_view(template_name="manager/manager.html"),name="manager"),
    path('manager_login/',views.manager_login.as_view(),name="manager_login"),
    path('recruitment/',TemplateView.as_view(template_name="manager/recruitment_page.html"),name="recruitment"),
    path('recruitment_details/',views.recruitment_details.as_view(),name="recruitment_details"),
    path('save_details/',views.save_details.as_view(),name="save_details"),
    path('modify_details/',TemplateView.as_view(template_name="manager/modify_details.html"),name="modify_details"),
    path('get_opp_details/',views.get_opp_details.as_view(),name="get_opp_details"),
    path('delete_details/',views.delete_details.as_view(),name="delete_details"),
    path('delete_recruitment/',views.delete_recruitment.as_view(),name="delete_recruitment"),
    path('interview_schedule/',views.interview_schedule.as_view(),name="interview_schedule"),
    path('get_applicant_details/',views.get_applicant_details.as_view(),name="get_applicant_details"),
    path('add_to_schdule/',views.add_to_schdule.as_view(),name="add_to_schdule")
]
