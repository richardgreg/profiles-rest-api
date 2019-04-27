from  rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermissions):
    """Allow users to edit their own profile."""

    def has_object_permission(self, request, view, obj):
        """Check if user is editing their own profile"""

        if request.method in permissions.SAFE_METHODS:
            return True

        # Checks and returns true if obj id == ti user and allow permission
        return obj.id == request.user.id