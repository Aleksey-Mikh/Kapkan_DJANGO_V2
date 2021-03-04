from django.urls import path, include
from .views import *


urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', user_login_view, name='login'),
    path('logout/', user_logout_view, name='logout'),

]
