from rest_framework import permissions



class permissionMixin:
    perms_map = {
        'GET':['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

class IsAllowed(permissions.DjangoModelPermissions,permissionMixin):
    def has_permission(self,request,view):
        return super().has_permission(request,view)

class CreateIsAllowed(permissions.BasePermission):
    def has_permission(self,request,view):
        print(request.user)
        if request.user.is_authenticated:
            return True
        return False
class IsAllowedToDelete(permissions.DjangoModelPermissions,permissionMixin):
    def has_object_permission(self,request,view,obj):
        if request.user == obj.author:
            return True
        return False