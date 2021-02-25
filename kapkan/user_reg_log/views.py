from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация прошла успешно')
            return redirect('login')
        else:
            messages.success(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'user_reg_log/register.html', {'form': form})


def login_view(request):
    return render(request, 'user_reg_log/login.html')