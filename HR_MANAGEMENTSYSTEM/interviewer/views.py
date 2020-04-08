from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import View
from HRadmin.models import adminModel
from applicant.models import ApplicantModel


class inter_login_check(View):
    def post(self,request):
        uname = request.POST["t1"]
        upass = request.POST["t2"]
        if adminModel.objects.filter(name=uname,passwod=upass,desgination="INTERVIWER").exists():
            return render(request,"interviewer/interviewer_home.html")
        else:
            messages.error(request,"please enter valid details")
            return redirect('interviewer')
    def get(self,request):

        return render(request, "interviewer/interviewer_home.html")


class  select_final_list(View):
    def get(self,request):
        am=ApplicantModel.objects.values("id")

        return render(request,"interviewer/select_final_list.html",{"am":am})