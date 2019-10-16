from rest_framework.permissions import BasePermission


class APIPermission(BasePermission):

    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return request.user.is_active
        if request.method in ['POST', 'PUT']:
            try:
                return request.user.hierarchy in [0, 1]
            except AttributeError:
                return False
        if request.method == 'DELETE':
            return request.user.is_staff
