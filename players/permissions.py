from rest_framework import permissions

class IsOwnerPelada(permissions.BasePermission):


    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            if obj.dono == request.user:
                return True
            else:
                return False
class PublicEndpoint(permissions.BasePermission):
    def has_permission(self, request, view):
        return True

class IsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        def has_object_permission(self, request, view, obj):

            if request.method in permissions.SAFE_METHODS:
                return True
            else:
                return obj.dono == request.user