from django.shortcuts import render
from.models import *


# Create your views here.
def index(request):
    return render(request,'index.html')

def blog(request):
    return render(request,'blog.html')

def about(request):
    return render(request,'about.html')

def contact(request):
     return render(request,'contact.html')

#==================signup===========================

def signup(request):
    if request.method=="POST":
        try:
            if request.POST['password']==request.POST['cpassword']:
                User.objects.create(
                fname = request.POST['fname'],
                lname = request.POST['lname'],
                email = request.POST['email'],
                mobile = request.POST['mobile'],
                password = request.POST['password']
                )

                msg = "Sign Up Successfully!!!!!"
                return render("login.html",{'msg':msg})

            else:
                msg = "Password & Confirm Password Don't match!!!!"
                return render("signup.html",{'msg':msg})
        
        except:
            msg = "Email is Allready register!!!!"
            return render("login.html",{'msg':msg})
        
        else:
            return render(request,'signup.html')


def shop(request):
     return render(request,'shop.html')

def wishlist(request):
     return render(request,'wishlist.html')

def product_single(request):
    return render(request,'product_single.html')

def checkout(request):
    return render(request,'checkout.html')

def cart(request):
    return render(request,'cart.html')

def blog_single(request):
    return render(request,'blog_single.html')
