from django.shortcuts import render,redirect
from .forms import UserForm
from django.contrib.auth import logout, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    form = UserForm()
    if request.method == 'POST':
       form = UserForm(request.POST)
       if form.is_valid():
           form.cleaned_data.get('username')
           form.save()
           return redirect('login')

    context = {'form':form}

    return render(request,'users/register.html',context)




def logoutview(request):
    logout(request)
    return render(request,'users/logout.html')