from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_opermission(self, request, view):
        # Only authenticated user can see list view
        if request.user.is_authenticated:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        # Read-only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the author of a post
        return obj.author == request.user