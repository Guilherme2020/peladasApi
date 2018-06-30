from rest_framework import permissions

class IsOwnerPelada(permissions.BasePermission):


    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            if obj.dono == request.user:
                return True
            else:
                return False