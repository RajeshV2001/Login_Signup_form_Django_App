from django.shortcuts import render
from .models import form_details

# Create your views here.

def index(request):
    return render(request,"base.html")


def signup(request):
    
    
    if request.method=='POST':
        
        mail=request.POST.get('mail')
        pswd=request.POST.get('password')
        pswd2=request.POST.get('password2')
        
        if mail=="" or pswd=="" or (pswd!=pswd2):
            return render(request,"signup.html")
        
        
        try:
            
            data=form_details(email=mail, password=pswd)
            data.save()
            msg="Signup succesfull !"
            return render(request,'lastpage.html',context={'msg':msg})
            
        except:
            
            msg="Email already exists. Please login !"
            return render(request,'lastpage.html',context={'msg':msg})
            
    
    else:
        
        return render(request,"signup.html")
    

def login(request):
    
    
    if request.method=='POST':
        
        mail=request.POST.get('mail')
        pswd=request.POST.get('password')
        
        
        if mail=="" or pswd=="":
            return render(request,"login.html")
            
        
                
        data=form_details.objects.filter(email=mail,password=pswd).exists()

        if data:
            
            msg="Login Successfull !"
            return render(request,'lastpage.html',context={'msg':msg})
        
        else:
            
            msg="Either mail or password is incorrect. Please signup !"
            return render(request,'lastpage.html',context={'msg':msg})

        
    
    else:
    
        return render(request,"login.html")


