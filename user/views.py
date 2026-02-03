from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
# Create your views here.

def login_user(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Aunthenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have Login Successfully')
            return redirect('blog-post')
        else:
            messages.error(request, 'There was an error login in please try again')
            return redirect('login-user')
    else:
        return render(request, 'user/login_user.html')
 
def logout_user(request):
    logout(request)
    messages.success(request, 'Goodbye')
    return redirect('/')
    


    
