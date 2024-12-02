from django.shortcuts import render, HttpResponse, redirect
from .forms import SignUp
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User




def sign_up(request):
    print("===================request")
    if request.method == 'POST':
        form = SignUp(request.POST)  # Bind data to form
        if form.is_valid():  # Validate form data
            # Check if the user already exists
            email = form.cleaned_data.get('email')
            if User.objects.filter(username=email).exists():
                messages.error(request, 'Email is already registered.')
            else:
                form.save()  # Save the user
                messages.success(request, 'Account created successfully. Please sign in.')
                return redirect('accounts:sign_in')  # Redirect after successful submission
        else:
            messages.error(request, 'Invalid form submission. Please try again.')
    else:
        form = SignUp()  # Empty form for GET request

    return render(request, 'sign-up.html', {'form': form})

def sign_in(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Authenticate user
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)  # Log in the user
            messages.success(request, 'Signed in successfully!')
            return redirect('web:index')  # Redirect to home or dashboard
        else:
            # If credentials don't match
            messages.error(request, 'Invalid email or password.')


    return render(request, 'sign-in.html')
