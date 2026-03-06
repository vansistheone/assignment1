from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from .models import User


def register(request):

    if request.method == "POST":

        full_name = request.POST['full_name']
        email = request.POST['email']
        password = request.POST['password']
        role = request.POST['role']

        User.objects.create(
            full_name = full_name,
            email = email,
            password_hash = password,
            role = role
        )

        return redirect('login')

    return render(request,'register.html')


def login_view(request):

    if request.method == "POST":

        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.filter(email=email).first()

        if user and check_password(password, user.password_hash):

            request.session['user_id'] = user.user_id
            request.session['role'] = user.role

            return redirect('dashboard')

        else:
            return render(request,'login.html',{'error':'Invalid credentials'})

    return render(request,'login.html')


def dashboard(request):

    if 'user_id' not in request.session:
        return redirect('login')

    return render(request,'dashboard.html')


def logout_view(request):

    request.session.flush()

    return redirect('login')