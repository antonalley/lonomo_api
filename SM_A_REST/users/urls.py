from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register("get_interests", views.InterestViewSet)
router.register("set_interests", views.PersonInterestViewSet)


urlpatterns = [
    path('', views.get_user_data),
    path('login/', views.login_api),
    path('register/', views.register_api),
    path("", include(router.urls))
]