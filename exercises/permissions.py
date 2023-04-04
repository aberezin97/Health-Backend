from django.shortcuts import get_object_or_404
from rest_framework import permissions
from user.models import User, Permission


class IsExerciseOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.day.user.id == request.user.id


class IsAllowedToReadWriteExercises(permissions.BasePermission):
    def has_permission(self, request, view):
        user_id = view.kwargs['user_id']
        print(user_id)
        if request.user.id == user_id:
            return True
        sender = get_object_or_404(User.objects.all(), pk=user_id)
        receiver = get_object_or_404(User.objects.all(), pk=request.user.id)
        try:
            permission = Permission.objects.get(receiver=receiver, sender=sender)
            if request.method in permissions.SAFE_METHODS:
                return permission.exercises >= 1
            else:
                return permission.exercises == 2
        except Permission.DoesNotExist:
            return False