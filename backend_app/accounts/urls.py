from django.urls import path
from .views import register_user, login_user, api_root

urlpatterns = [
    path('', api_root, name='api_root'),
    path('register/', register_user, name='register_user'),
    path('login/', login_user, name='login_user'),
]
