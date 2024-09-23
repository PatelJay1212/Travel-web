# from django.shortcuts import render,HttpResponse,redirect
# from django.contrib.auth.models import User
# from myadmin.models import Packages
# from myuser import models
# from django import forms
# from myuser.forms import BookForm 
# from django.contrib.auth import login,logout,authenticate


from django.shortcuts import get_object_or_404, redirect, render,HttpResponse
from myuser.models import Payment, Book
from myuser import models
from myadmin.models import Packages
from myuser.forms import BookForm
from myuser.forms import PaymentForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django import forms
from django.core.paginator import Paginator
# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
# Create your views here.

def user_about(request):
    return render(request,'myuser/about.html')
    # Package = Packages.objects.all()
    # context = {'package':Package}
    # return render(request,'myuser/index.html',context)

def user_mybooking(request):
    data = models.Book.objects.filter(user=request.user)
    paginator = Paginator(data, 10)  # Show 10 bookings per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj}
    return render(request, 'myuser/mybooking.html', context=context)
 

def user_contact(request):
    return render(request,'myuser/contact.html')

def user_destination(request):
    return render(request,'myuser/destination.html')

def user_index(request):
    Package=Packages.objects.all()
    context={'package':Package}
    return render(request,'myuser/index.html',context)

def user_package(request):
    Package=Packages.objects.all()
    context={'package':Package}
    return render(request,'myuser/package.html',context)

def data_table(request):
    return render(request,'myuser/data_tables.html')

def user_service(request):
    data = Packages.objects.all()
    context={'data':data}
    return render(request,'myuser/service.html',context)

def user_team(request):
    return render(request,'myuser/team.html')

def user_testimonial(request):
    return render(request,'myuser/testimonial.html')


def package_detail(request,id):
    data = Packages.objects.get(id=id)
    context = {'data':data}
    return render(request,'myuser/package_detail.html',context)

def book_package(request,id):
    pack = models.Packages.objects.get(id=id)
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.package = pack
            
            obj.save()
            return redirect(payment,id)
        else:
            print(form.errors)
             
             
    else:
         form = models.Book()        
    return render(request,'myuser/bookpackage.html')


def payment(request,id):
    package = get_object_or_404(Packages, id=id)
    confirm = Book.objects.filter(user=request.user, package=id).last()
    if request.method == 'POST':
       
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.user = request.user
            payment.package = package
            payment.save()
    
            if confirm:
                confirm.is_booked = True
                confirm.payment= payment
                confirm.save()
            return redirect(conf_book,id)  
        else:
            print(form.errors)
    else:
        form = PaymentForm()
    context = {'package': package, 'form': form}
    return render(request, 'myuser/payment.html', context)

def loginviews(request):
    if request.method == "POST":
     username = request.POST.get('username')
     password = request.POST.get('password')
     user = authenticate(username=username,password=password)
     if user is not None:
        login(request,user)
        return redirect(user_index)
     else:
        return HttpResponse("User not found")
    return render(request,'myuser/login.html')

def register(request):
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
                return redirect(loginviews)
        else:
            return HttpResponse("password do not match")
    return render(request,'myuser/register.html')

def conf_book(request,id):
    data = models.Book.objects.get(id=id)
    context = {'data':data}
    return render(request,'myuser/confirmed_booking.html',context)

def pdf(request):
    return render(request,'myuser/generate_pdf.html')

def search_packages(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        print(search)
        data= models.Packages.objects.filter(title__icontains=search)
    else:
        data=models.Packages.objects.all()
    context= {'package':data}
    return render(request,'myuser/package.html',context)






# def generate_pdf(book):
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="book_details.pdf"'

#     # Create a PDF object
#     p = canvas.Canvas(response, pagesize=letter)

#     # Write your content
#     p.drawString(100, 750, "Book Title: {}".format(book.title))
#     p.drawString(100, 730, "Author: {}".format(book.author))
#     # Add more fields as needed

#     # Close the PDF object cleanly and finalize the PDF document
#     p.showPage()
#     p.save()

#     return response

