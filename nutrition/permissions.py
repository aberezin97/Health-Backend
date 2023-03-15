from rest_framework import permissions
from django.shortcuts import get_object_or_404
from user.models import User, Permission


class IsAllowedToModifyDeleteNutrition(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.day.user.id == request.user.id:
            return True
        sender = get_object_or_404(User.objects.all(), pk=obj.day.user.id)
        try:
            permission = Permission.objects.get(sender=sender, receiver=request.user)
            return permission.nutrition >= 2
        except Permission.DoesNotExist:
            return False


class IsAllowedToReadWriteNutrition(permissions.BasePermission):
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
                return permission.nutrition >= 1
            else:
                return permission.nutrition == 2
        except Permission.DoesNotExist:
            return False
