from django.shortcuts import render
from.forms import LoginForm,SignupForm
from django.contrib.auth import login,authenticate,logout
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.
def signin(request):
    if request.method =='POST':
        form =LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = cd['username']
            password = cd['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return render(request,'index.html')
            else:
                pass

    form = LoginForm()
    return render(request,'account/login.html',{'form':form})

def signup(request):
    if request.method =='POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            print('form data is valid')
            user =form.save(commit=False)
            user.set_password(
                form.cleaned_data['password']
            )
            user.save()
            login(request,user)
            return render(request,'index.html')
        else:
            sign= SignupForm()
            return render(request,'account/signup.html',{'form':form})
            

    sign= SignupForm()
    return render(request,'account/signup.html',{'sign':sign})

    


def signout(request):
    logout(request)
    return render(request,'index.html')