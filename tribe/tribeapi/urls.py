from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'hobbies', views.HobbyViewSet)
router.register(r'persons', views.PersonViewSet)
router.register(r'personhobby', views.PersonHobbyViewSet, basename="personHobby")
# router.register(r'personhobbies', views.personHobbies, basename="personHobbies")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('person/hobbies/', views.PersonsHobbiesView.as_view(), name="person_hobbies"), # TODO is there a better way to show all hobbies for a person?
    path('person/similarhobbies/', views.SimilarHobbies.as_view(), name="similarHobbies"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]