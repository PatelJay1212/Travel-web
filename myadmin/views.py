from django.shortcuts import render,HttpResponse,redirect
from myadmin import forms 
from myadmin import models
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate


# Create your views here.

def trialview(request):
    return HttpResponse('trial suceess')

def indexview(request):
    if request.user.is_authenticated:
        total_packages = models.Packages.objects.all().count()
        context = {'total_packages': total_packages}
        return render(request,'myadmin/index.html',context)
    else:
        return redirect(indexview)

def signupview(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        if password == password1:
            try:
                User.objects.get(username=username)
                return HttpResponse("username already exists")
            except:
                User.objects.create_user(username=username,password=password)
                return redirect(signinview)
        else:
            return HttpResponse("password do not match")
        
    return render(request,'myadmin/sign-up.html')

def signinview(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect(indexview)
        else:
            return HttpResponse("User not found")
    
    return render(request,'myadmin/sign-in.html')

def formview(request):
    if request.method == "POST":
       form = forms.CategoryForm(request.POST)
       if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect(tableview)
       else:
            print("error")
            print(form.errors)
    return render(request,'myadmin/form.html')


def form2view(request):
    if request.method == "POST":
        form = forms.PackagesForm(request.POST,request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect(table2view)
        else:
            print("error")
            print(form.errors)
    return render(request,'myadmin/form2.html')
    

def Categorydelete(request,id):
    data = models.Category.objects.get(id=id)
    data.delete()
    return redirect(tableview)

def Packagesdelete(request,id):
    data = models.Packages.objects.get(id=id)
    data.delete()
    return redirect(table2view)

def Categoryedit(request,id):
    data = models.Category.objects.get(id=id)
    context = {'data':data}
    return render(request,'myadmin/editcategory.html',context=context)

def Packagesedit(request,id):
    data = models.Packages.objects.get(id=id)
    context = {'data':data}
    return render(request,'myadmin/editpackages.html',context=context)

# def virtualview(request):
#     return render(request,"virtual-reality.html")

def tableview(request):
    data= models.Category.objects.all()
    context= {'data':data}
    return render(request,'myadmin/tables.html',context=context)

def table2view(request):
    data= models.Packages.objects.all()    #filter(user=request.user)
    context= {'data':data}
    return render(request,'myadmin/tables2.html',context=context)


def Categoryupdate(request,id):
    data = models.Category.objects.get(id=id)
    if request.method == "POST":
        form = forms.CategoryForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect(tableview)
        else:
            print("error")
            print(form.errors)    
    return render(request,'myadmin/editcategory.html')


def Packagesupdate(request,id):
    data = models.Packages.objects.get(id=id)
    if request.method == "POST":
        form = forms.PackagesForm(request.POST,instance=data)
        if form.is_valid():
            
            form.save()
            return redirect(table2view)
        else:
            print("error")
            print(form.errors)    
    return render(request,'myadmin/editpackages.html')


# def rtlview(request):
#     return render(request,"rtl.html")

# def billingview(request):
#     return render(request,"billing.html")

def dashview(request):
    return render(request,'myadmin/dashboard.html')

def eleview(request):
    return render(request,"forms-elements.html")

def logoutview(request):
    logout(request)
    return redirect(signinview)


