from rest_framework import permissions


class IsExerciseOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.day.user.id == request.user.id
