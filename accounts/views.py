from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'login successfull')
            return redirect('/consultations/search')
        else:
            messages.success(request, 'Error in lgoin')
            return redirect('/')
        
    else:    
        return render(request, 'accounts/login.html', {})
    


    # if request.method == 'POST':
    #     form = AuthenticationForm(data=request.POST)
    #     if form.is_valid():
    #         user = form.get_user()
    #         login(request, user)
    #         return redirect('/consultations/patient_list')  # Change 'home' to your desired redirect URL
    # else:
    #     form = AuthenticationForm()
    # return render(request, 'accounts/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'logout successfull')
    return redirect('/')

def home(request):
    return render(request, 'accounts/test.html', {})




# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             messages.success(request, 'login successfull')
#             return redirect('/consultations/patient_list')
#         else:
#             messages.success(request, 'Error in lgoin')
#             return redirect('/')
        
#     else:    
#         return render(request, 'accounts/login.html', {})
    