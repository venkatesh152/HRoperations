from django.shortcuts import render, redirect
from django.views import View
from HRadmin.forms import adminForm
from HRadmin.models import adminModel

class admin_login(View):
    def post(self,request):
        uname=request.POST["t1"]
        passwod=request.POST["t2"]
        if uname == "admin" and passwod == "admin":
            return render(request,"HRadmin/Admin_Home.html")
        else:
            return redirect('hr_admin')
    def get(self,request):
        return render(request, "HRadmin/Admin_Home.html")

class add_employee(View):

    def get(self,request):
        return render(request,"HRadmin/Add_Employee.html",{"ef":adminForm()})


class save_emp(View):

    def post(self,request):
        af = adminForm(request.POST)

        if af.is_valid():
            af.save()

            return redirect('admin_login')
        else:

            return render(request, "HRadmin/Add_Employee.html", {"ef": af})

class view_employee(View):
    def get(self,request):
      qs=adminModel.objects.all()
      return render(request,"HRadmin/view_Employee.html",{"form":qs})

class update_employee1(View):
    def get(self,request):
        qs=adminModel.objects.values("id","name","desgination")
        return render(request,"HRadmin/update_employee_view.html",{"form":qs})
class update_employee2(View):
    def get(self,request):
       idno = request.GET["id"]
       qs=adminModel.objects.get(id=idno)
       # ad=adminForm(instance=qs)
       return render(request,"HRadmin/update_employee.html",{"form":qs})


class update(View):
    def post(self,request):
       i = request.POST["t1"]
       n = request.POST["t2"]
       d = request.POST["t3"]
       a = request.POST["t4"]
       c = request.POST["t5"]
       e = request.POST["t6"]

       am=adminModel.objects.filter(id=i)

       am.update(name=n,desgination=d,address=a,contact=c,email=e)
       return redirect('admin_login')


class delete_page(View):
    def get(self,request):
        am=adminModel.objects.values("id","name","desgination","address")
        return render(request,"HRadmin/delete_page.html",{"data":am})


class delete_emp(View):
   def post(self,request):
       c=request.POST.getlist("t1")
       print(c)
       for x in c:
           adminModel.objects.filter(id=x).delete()
       return redirect('delete_page')
