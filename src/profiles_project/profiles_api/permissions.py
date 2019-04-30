from  rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile."""

    def has_object_permission(self, request, view, obj):
        """Check if user is editing their own profile"""

        if request.method in permissions.SAFE_METHODS:
            return True

        # Checks and returns true if obj id == to user and allow permission
        return obj.id == request.user.id