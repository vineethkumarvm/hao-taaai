from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import categories , jobs

# Create your views here.
def index(request):
    category = categories.objects.all()
    return render(request,'index.html',{'category': category})

def about(request):
    return render(request,'about.html')

def job(request,id=None):
    if id:
        categ = get_object_or_404(categories,id=id)
        joy = jobs.objects.filter(cat=categ)
        context = {
            'jo' : joy,
        }
        return render(request,'job.html',context)
    else:
        joy = jobs.objects.all()
        context = {
            'jo' : joy,
        }
        return render(request,'job.html',context)

def crptojob(request,id):
    jos = jobs.objects.get(id = id)
    context = {
        'joi' : jos
    }
    return render(request,'crptojob.html',context)


# def login(request):
#     return render(request,'login.html')

# def signup(request):
#     return render(request,'signup.html')