from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

#from django.views.decorators.csrf import csrf_exempt

#@csrf_exempt
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            pass
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ("Failed to login"))
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})