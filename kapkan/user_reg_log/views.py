from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm, UserLoginForm, UserEditForm
from .models import Profile


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(user=user)
            login(request, user)
            messages.success(request, 'Регистрация прошла успешно')
            return redirect('home')
        else:
            messages.success(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'user_reg_log/register.html', {'form': form})


def user_login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'user_reg_log/login.html', {'form': form})


def user_logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def edit(request):
    customer = Profile.objects.get(user=request.user)
    customer = customer.orders.all()
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('profile')
    else:
        user_form = UserEditForm(instance=request.user)
        bonus_points = Profile.objects.get(user=request.user).bonus_points
        context = {
            'user_form': user_form,
            'bonus_points': bonus_points,
            'customer': customer,
        }
        return render(request, 'user_reg_log/user_profile.html', context)
