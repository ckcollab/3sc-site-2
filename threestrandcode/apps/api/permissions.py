from rest_framework.permissions import BasePermission


class IsSuperUserOrPOSTing(BasePermission):

    def has_permission(self, request, view):
        return request.method == 'POST' or request.user.is_superuser
