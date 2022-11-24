from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GetUserPlansView, request_join_event, leave_event

router = DefaultRouter()
router.register("getuserplans", GetUserPlansView)


urlpatterns = [
    path('', include(router.urls)),
    path('request_join_event/', request_join_event),
    path('leave_event/', leave_event),

]
