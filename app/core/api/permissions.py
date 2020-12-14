from rest_framework import permissions


class AnonPermissionOnly(permissions.BasePermission):
    """
    Non-authenticated Users only.
    """
    message = "You are already logged."

    def has_permission(self, request, view):
        return not request.user.is_authenticated  # property, not a method ()


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """
    message = "You must be owner of this content to change it."

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.owner == request.user
