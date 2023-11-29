from django.http import JsonResponse, Http404
from .db.models import User


def get_user(request, user_id):
    try:
        user = get_user_for_id(user_id)
        return JsonResponse({"id": user.id, "name": user.name, "email": user.email})
    except User.DoesNotExist:
        raise Http404("User does not exist")


def get_stuff(request, stuff_id):
    try:
        user = User.objects.get(id=stuff_id)
        return JsonResponse({"id": user.id, "name": user.name, "email": user.email})
    except User.DoesNotExist:
        raise Http404("User does not exist")


def get_user_for_id(user_id):
    return User.objects.get(id=user_id)
