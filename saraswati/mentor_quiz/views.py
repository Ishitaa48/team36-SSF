from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import NineTenform,Interform
from .models import NineTen,Inter

# Create your views here.
def add_show(request):
    if request.method =='POST':
        fm=NineTenform(request.POST)
        fm1=Interform(request.POST)
        if fm.is_valid():
            fm.save()
        if fm1.is_valid():
            fm1.save()
    else:
        fm=NineTenform()
        fm1=Interform()
    school=NineTen.objects.all()
    inter=Inter.objects.all()
    return render(request,'addquiz.html',{'form1':fm,'form2':fm1, 'school':school,'inter':inter})

def update_data(request, id):
    if request.method=='POST':
        pi=NineTen.objects.get(pk=id)
        fm=NineTenform(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=NineTen.objects.get(pk=id)
        fm=NineTenform(instance=pi)
    return render(request,'updatestudent.html',{'form':fm})

def update_data_inter(request, id):
    if request.method=='POST':
        pi=Inter.objects.get(pk=id)
        fm=Interform(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=Inter.objects.get(pk=id)
        fm=Interform(instance=pi)
    return render(request,'updatestudentinter.html',{'form':fm})


def delete_data(request, id):
    if request.method == 'POST':
        pi=NineTen.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

def delete_data_inter(request, id):
    if request.method == 'POST':
        pi=Inter.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
