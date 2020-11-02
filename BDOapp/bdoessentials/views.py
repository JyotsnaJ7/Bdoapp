from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from bdoessentials.models import Lead
from bdoessentials.forms import LeadCreateFrm,RegistrationFrm
from django.contrib.auth import  authenticate,login
from django.utils.decorators import method_decorator

# Create your views here.

@login_required
def createLead(request):

    form=LeadCreateFrm()
    context={}
    context['form']=form
    qs = Lead.objects.all()
    context['leads'] = qs

    if request.method=='POST':
        form=LeadCreateFrm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('createlead')

    return render(request,'bdoessentials/leadreg.html',context)

def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('uname')
        password=request.POST.get('pwd')
        print(username,',',password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('createlead')
        else:
            return redirect('loginpage')

    return render(request,'bdoessentials/login.html')

def register(request):
    form=RegistrationFrm()

    context={}
    context['form']=form

    if request.method=='POST':
        form=RegistrationFrm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginpage')
        else:
            context['form']=form
            return render(request, 'bdoessentials/registration.html', context)
    return render(request,'bdoessentials/registration.html',context)

def leadDetails(request,pk):
    obj=Lead.objects.get(id=pk)

    context={}
    context['lead']=obj

    return render(request,'bdoessentials/leaddetails.html',context)

def leadEdit(request,pk):
    form=Lead.objects.get(id=pk)
    form=LeadCreateFrm(instance=form)

    context={'Edit':form}
    if request.method == "POST":
        form=Lead.objects.get(id=pk)
        form=LeadCreateFrm(instance=form,data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('createlead')
    return render(request,'bdoessentials/leadedit.html',context)

def landingpage(request):
    return render (request,'bdoessentials/base.html')

def followupview(request,pk):
    obj=Lead.objects.get(id=pk)

    context={}
    context['lead']=obj

    return render(request,'bdoessentials/followup.html',context)


def upcomingfollowupview(request,pk):
    obj=Lead.objects.get(id=pk)

    context={}
    context['lead']=obj

    return render(request,'bdoessentials/upcomingfollowup.html',context)

def leadDelete(request,pk):
    dele=Lead.objects.get(id=pk)
    dele.delete()
    form=LeadCreateFrm()
    context={'form':form}
    qs=LeadCreateFrm()
    context['delete']=qs
    return redirect('createlead')