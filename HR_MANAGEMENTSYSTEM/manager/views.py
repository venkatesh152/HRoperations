from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import View
from HRadmin.models import adminModel
from applicant.models import ApplicantModel
from .forms import recuirtmentform,InterviewSeheduleForm
from .models import recuirtmentModel,InterviewSeheduleModel

class manager_login(View):
    def post(self,request):
        uname = request.POST["t1"]
        password = request.POST["t2"]
        
        if adminModel.objects.filter(name=uname,passwod=password,desgination="MANAGER").exists():
             return render(request,"manager/manager_home.html")
        else:
             return redirect('manager')
    def get(self,request):
        return render(request, "manager/manager_home.html")


class recruitment_details(View):
    def get(self,request):
        return render(request,"manager/recruient_form.html",{"form":recuirtmentform()})


class save_details(View):
    def post(self,request):
        rf=recuirtmentform(request.POST)
        if rf.is_valid():
            rf.save()
            return redirect('recruitment')
        else:
            return render(request, "manager/recruient_form.html", {"form":rf})


class get_opp_details(View):
    def post(self,request):
        opp_code=request.POST["t1"]

        op=recuirtmentModel.objects.get(oppertunitycode=opp_code)
        return render(request,"manager/modify_details.html",{"form":op})



class delete_details(View):
    def get(self,request):
        re=recuirtmentModel.objects.values('oppertunitycode','qualification','startregistration','agelimit')
        return render(request,"manager/delete_details.html",{"form":re})


class delete_recruitment(View):
    def post(self,request):
        li=request.POST.getlist("t1")
        for x in li:
            recuirtmentModel.objects.filter(oppertunitycode=x).delete()

        return redirect('delete_details')


class interview_schedule(View):
    def get(self,request):
        ap = ApplicantModel.objects.values("id")

        return render(request,"manager/interview_schedule.html",{"ap":ap})


class get_applicant_details(View):
    def post(self,request):
        ap_id=request.POST["t1"]
        ap = ApplicantModel.objects.values("id")
        am = adminModel.objects.filter(desgination="INTERVIWER")
        return render(request,"manager/interview_schedule.html",{"form":InterviewSeheduleForm(),"am":am,"ap_id":ap_id,"ap":ap})


class add_to_schdule(View):
    def post(self,request):
        id=request.POST["applicantId"]
        eid=request.POST["a1"]
        s=request.POST["scheduleDate"]
        InterviewSeheduleModel(applicantId=id,employeeId=eid,scheduleDate=s).save()


        # isf=InterviewSeheduleForm(request.POST)
        # if isf.is_valid():
        #     isf.save()
        messages.success(request,"Data saved successfully")
        return redirect('manager_login')
        #else:
            # ap_id = request.POST["applicantId"]
            # ap = ApplicantModel.objects.values("id")
            # am = adminModel.objects.filter(desgination="INTERVIWER")
           # return render(request, "manager/interview_schedule.html",
                        #   {"form":isf})
