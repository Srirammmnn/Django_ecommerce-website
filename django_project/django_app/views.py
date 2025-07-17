from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Product
from .forms import SignupForm 
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.db.models import Q


def index(request):
    products=Product.objects.all()
    return render(request,'index.html',{'products':products})

def user_login(request):
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)
        if user is not None:
          login(request,user)
          messages.success(request,("you have been logged in"))
          return redirect('index')
        else:
          messages.success(request,("There is an error"))
          return redirect('login')
    else:
       return render(request,'login.html',{})

def logout_user(request):
    logout(request)
    messages.success(request,("you have been logged out...."))  
    return redirect('index')


def sign(request):
    form = SignupForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
            form.save()
            messages.success(request,'Registration successfull...')
            return redirect('login')  # or your desired page
    return render(request, 'sign.html', {'form': form})


def contact(request):
    return render(request,'contact.html',{})


def about(request):
    return render(request,'about.html',{})

def product(request,pk):
    product = Product.objects.get(id=pk)
    return render(request,'product.html',{'product':product})


def search(request):

    # Determine if they filled out the form
    if request.method == "POST":
        searched = request.POST['searched'] #to get the searched name in html.

        # Query The Products DB Model

        searched = Product.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched))

        # Test for null

        if not searched:
            messages.success(request, "That Product Does Not Exist...Please try Again.")
            return render(request, "search.html", {})

        else:
            return render(request, "search.html", {'searched':searched})

    else:
        return render(request, "search.html", {})

