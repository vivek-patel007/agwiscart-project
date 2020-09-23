from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def homepage(request):
    return render(request, 'home/home.html')
def contact(request):
    if request.method=='POST':
      fullname=request.POST['fullname']
      subject=request.POST['subject']
      cemail=request.POST['cemail']
      msg=request.POST['msg']
      #print(fname,lname,mobile,cemail,msg)
      if fullname=="" or len(subject)<4 or cemail=="" or len(msg)<10 :
         messages.error(request, "please fill up the details correctly")
      else:
         data=Contact(fullname=fullname, subject=subject, cemail=cemail,msg=msg)
         data.save()
         messages.success(request, "your massage has been successfully sent..")
    return render(request, 'home/contact.html')

def about(request):
   return render(request, 'home/about.html')


def signuphandle(request):
   if request.method == 'POST':
      first_name=request.POST['signupfname']
      last_name=request.POST['signuplname']
      user_name=request.POST['uname']
      e_mail=request.POST['signupemail']
      password=request.POST['signuppass']
      c_password=request.POST['signupcpass']

      
     
      
      # print(first_name,last_name,user_name,e_mail,password,c_password)
      
      #check errors
      if User.objects.filter(username=user_name).exists():
         messages.error(request, "This UserName Is Already Avalable.")
         return redirect("homepage")
      if User.objects.filter(email=e_mail).exists():
         messages.error(request, "User E-Mail Is Already Avalable.")
         return redirect("homepage")
      if len(user_name) > 10:
         messages.error(request, "User Name Must Be 10 Characters.")
         return redirect("homepage")
      if not user_name.isalnum():
         messages.error(request, "Username Should Only Contain Letters And Numbers.")
         return redirect("homepage")
      if password != c_password:
         messages.error(request, "Password do Not Match Please Confirm The password.")
         return redirect("homepage")
      #create users
      myuser=User.objects.create_user(user_name,e_mail,password)
      myuser.first_name=first_name
      myuser.last_name=last_name
      myuser.save()
      messages.success(request, "sign up successfully now u log in....")
      return redirect("loginpage")
   return render(request, 'home/home.html')

def loginhandle(request):
   if request.method == 'POST':
      fm=AuthenticationForm(request=request, data=request.POST)
      if fm.is_valid():
         uname=fm.cleaned_data['username']
         upass=fm.cleaned_data['password']

         user=authenticate(username=uname,password=upass)
         if user is not None:
            login(request, user)
            messages.success(request, "login success")
            return HttpResponseRedirect(reverse('homepage'))
   else:
      fm=AuthenticationForm()
   return render(request,'home/login.html', {'form':fm})

def logouthandle(request):
    logout(request)
    messages.success(request, "logout success")
    return redirect("loginpage")
