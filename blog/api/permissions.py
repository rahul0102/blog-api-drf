from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAdminUser

class IsOwnerOrReadOnly(BasePermission):
    message = "You are not owner of this object"
    # exclude_methods = ['OPTIONS', 'HEAD']
    # def has_permissions(self, request, view):
    #     if request.method not in exclude_methods:
    #         return True
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        # # if user is admin give him rights to do anything
        if request.user.is_staff:
            return True
        # print(type(obj.author), "\n ", type(request.user), "\n-> ", str(obj.author) == str(request.user))
        return (str(obj.author) == str(request.user))

class IsAdminOrAccountOwner(BasePermission):
    message = "You are not authenticated to view or modify other user"
    exclude_methods = ['OPTIONS', 'HEAD']
    def has_permissions(self, request, view):
        if request.method not in exclude_methods:
            return True
    def has_object_permission(self, request, view, obj):
         # # if user is admin give him rights to do anything
        # if request.method in SAFE_METHODS:
        #     return True
        print('here')

        if request.user.is_staff:
            return True
        print(str(obj.username), str(request.user))
        print('here')
        return str(obj.username) == str(request.user)
