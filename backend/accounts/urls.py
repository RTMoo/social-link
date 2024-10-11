from django.urls import path
from accounts.views import RegisterAPIView, LoginAPIView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]