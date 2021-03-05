from django.urls import path, include
from .views import register_view, user_login_view, user_logout_view, user_profile


urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', user_login_view, name='login'),
    path('logout/', user_logout_view, name='logout'),
    path('profile/<str:username>', user_profile, name='profile'),
]
