from rest_framework import permissions
from user.models import Permission, User
from django.shortcuts import get_object_or_404


class IsAllowedToReadStats(permissions.BasePermission):
    def has_permission(self, request, view):
        user_id = view.kwargs['user_id']
        print(user_id)
        if request.user.id == user_id:
            return True
        if request.method in permissions.SAFE_METHODS:
            sender = get_object_or_404(User.objects.all(), pk=user_id)
            receiver = get_object_or_404(User.objects.all(), pk=request.user.id)
            try:
                permission = Permission.objects.get(receiver=receiver, sender=sender)
                return permission.stats
            except Permission.DoesNotExist:
                return False
        return False
