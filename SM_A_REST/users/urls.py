from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_user_data),
    path('login/', views.login_api),
    path('register/', views.register_api),
]