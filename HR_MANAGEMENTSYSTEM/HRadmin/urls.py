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
from django.urls import path
from  django.views.generic import TemplateView

from HRadmin import views

urlpatterns = [
    path('hr_admin/',TemplateView.as_view(template_name="HRadmin/Admin_Login_page.html"),name="hr_admin"),
    path('admin_login/',views.admin_login.as_view(),name="admin_login"),
    path('add_employee/',views.add_employee.as_view(),name="add_employee"),
    path('save_emp/',views.save_emp.as_view(),name="save_emp"),
    path('view_employee/',views.view_employee.as_view(),name='view_employee'),
    path('update_employee1/',views.update_employee1.as_view(),name='update_employee1'),
    path('update_employee2/',views.update_employee2.as_view(),name="update_employee2"),
    path('update/',views.update.as_view(),name="update"),
    path('delete_page/',views.delete_page.as_view(),name="delete_page"),
    path('delete_emp/',views.delete_emp.as_view(),name="delete_emp"),
]
