from django.urls import path, include
from .views import register_view, user_login_view, user_logout_view, edit


urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', user_login_view, name='login'),
    path('logout/', user_logout_view, name='logout'),
    path('profile/', edit, name='profile'),
]
