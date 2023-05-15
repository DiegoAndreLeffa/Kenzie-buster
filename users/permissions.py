from rest_framework import permissions
from rest_framework.views import Request, View
from users.models import User


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_authenticated and request.user.is_superuser:
            return True


class IsOwnerOrAdminUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_employee:
            return True

        if obj == request.user:
            return True

        return False
