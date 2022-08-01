from rest_framework.permissions import BasePermission


class IsManagement(BasePermission):
    pass


class IsSales(BasePermission):
    pass


class IsSupport(BasePermission):
    pass
