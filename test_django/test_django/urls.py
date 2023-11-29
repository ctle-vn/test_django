from django.urls import path
from .views import get_user, get_stuff

urlpatterns = [
    path("user/<int:user_id>/", get_user, name="get_user"),
    path("stuff/<int:stuff_id>/", get_stuff, name="get_stuff"),
]
