from django.shortcuts import render,redirect
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
                return render(request,"login.html")

            else:
                msg = "Password & Confirm Password Don't match!!!!"
                return render(request,"signup.html",{'msg':msg})
        
        except:
            msg = "Email is Allready register!!!!"
            return render(request,"login.html",{'msg':msg})
        
    else:
        return render(request,'signup.html')

    #==========================Login============================

def login(request):
    if request.method=="POST":
        try:
            user = User.objects.get(email=request.POST['email'])
            if user.password==request.POST['password']:
                request.session['email']=user.email
                return render(request,'index.html')

            else:
                msg = "Email & Password Don't Match"
                return render(request,'login.html',{'msg':msg})
            
                #else:
                    #msg = "Password Don't Match!!!"
                    #return render(request,'login.html',{'msg':msg})

        except:
            msg = "Email is not Register"
            return redirect('signup')
    
    else:
        return render(request,'login.html')


#=======================Logout=================================

def logout(request):
    del request.session['email']
    return redirect('login')

#=====================Change-password============================

def cpassword(request):
    if request.method=="POST":
        user = User.objects.get(email=request.session['email'])

        if user.password==request.POST['opassword']:
            if request.POST['npassword']==request.POST['cnpassword']:
                user.password = request.POST['npassword']
                user.save()
                return redirect('logout')
            else:
                msg = "New Password & Confirm New Password Doesn't match!!!!!"
                return render(request,'cpassword.html',{'msg':msg})
        else:
            msg = "Old Password Doesn't Match!!!"    
            return render(request,'cpassword.html',{'msg':msg})
    else:
        return render(request,'cpassword.html')

#=====================Forgot Password==============================

def fpassword (request):
    return render(request,'fpassword.html')

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
