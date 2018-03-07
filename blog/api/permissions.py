from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    message = "You are not owner of this object"
    # my_safe_methods = ['GET', 'PUT']
    # def has_permissions(self, request, view):
    #     if request.method in my_safe_methods:
    #         return True
    #     return False
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        # print(type(obj.author), "\n ", type(request.user), "\n-> ", str(obj.author) == str(request.user))
        return str(obj.author) == str(request.user)
