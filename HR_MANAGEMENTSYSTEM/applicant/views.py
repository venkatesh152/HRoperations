from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic.base import View
from .forms import ApplicantForm,Application_Form
from .models import ApplicantModel

class New_appicant_reg(View):
      def get(self,request):
          return render(request,"applicant/New_appicant_reg.html",{"form":ApplicantForm()})


class  register(View):
    def post(self,request):
        af=ApplicantForm(request.POST)
        if af.is_valid():
            af.save()
            return redirect('applicant')
        else:
            return render(request, "applicant/New_appicant_reg.html", {"form":af})


class  login_check(View):
    def post(self,request):
        uname = request.POST["t1"]
        upass = request.POST["t2"]
        if ApplicantModel.objects.filter(username=uname,password=upass).exists():

            return render(request,"applicant/application_form.html",{"form":Application_Form()})
        else:
            messages.error(request,"Invalid USer")
            return redirect('applicant')
    def get(self,request):
        return render(request, "applicant/application_form.html", {"form": Application_Form(),"mess":"Applyed successfully"})



class apply(View):
   def post(self,request):
       af=Application_Form(request.POST,request.FILES)
       if af.is_valid():
           af.save()
           return redirect('login_check')
       else:
           return render(request,"applicant/application_form.html",{"form":af})