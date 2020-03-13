from rest_framework import permissions

class IsSupervisorOrRejected(permissions.BasePermission):
    """
    If user is not a supervisor, request is rejected.
    """
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff
