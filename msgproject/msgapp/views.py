from django.shortcuts import redirect, render
from django.contrib import messages

def home(request):
    return render(request,'msg/home.html')

def receiveData(request):
    if request.method == 'POST':
        fullName=request.POST['full_name']
        email=request.POST['email']
        msg=request.POST['msg']

        if fullName and email and msg != '':
            print('success')
            messages.success(request,'Your message send successfully!')
        else:
            messages.error(request,'Please fill the all feilds')
            
    
    return redirect(home)