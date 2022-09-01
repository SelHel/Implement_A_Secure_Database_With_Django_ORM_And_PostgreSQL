import re
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.exceptions import PermissionDenied

from clients.models import Client
from contracts.models import Contract
from events.models import Event


class IsManagement(BasePermission):
    def has_permission(self, request, view):
        return request.user.employee.role == 'MANAGEMENT' and request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)


class ClientPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.employee.role == 'SUPPORT':
            return request.method in SAFE_METHODS
        return request.user.employee.role == 'SALES'

    def has_object_permission(self, request, view, obj):
        if request.method == 'DELETE':
            return False
        elif request.user.employee.role == 'SUPPORT' and request.method in SAFE_METHODS:
            return obj in Client.objects.filter(
                contract__event__support_contact=request.user.employee
                ).distinct()
        elif request.user.employee.role == 'SALES':
            return obj in Client.objects.filter(
                sales_contact=request.user.employee
                )
        else:
            return False


class ContractPermision(BasePermission):
    def has_permission(self, request, view):
        pk = view.kwargs.get('pk')
        if pk is not None:            
            contract = Contract.objects.get(id=view.kwargs['pk'])
            employee = request.user.employee
            if employee.role == 'SALES':
                if contract.sales_contact != employee:
                    return False

            elif employee.role == "SUPPORT":
                try:
                    event = contract.event
                    if event.support_contact != employee:
                        return False
                except:
                    return False

        if request.user.employee.role == 'SUPPORT':
            return request.method in SAFE_METHODS
        return request.user.employee.role == 'SALES'

    def has_object_permission(self, request, view, obj):
        if request.method == 'DELETE':
            return False
        elif request.method in SAFE_METHODS:
            return True
        elif obj.is_signed is True:
            raise PermissionDenied("You cannot update a signed contract !")
        elif request.user.employee.role == 'SALES':
            return obj.sales_contact == request.user.employee
        return False


class EventPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.employee.role == 'SUPPORT':
            return request.method in ['GET', 'PUT', 'PATCH']
        return request.user.employee.role == 'SALES'

    def has_object_permission(self, request, view, obj):
        if request.method == 'DELETE':
            return False
        elif request.method in ['PUT', 'PATCH'] and obj.is_finished is True:
            raise PermissionDenied("You cannot update a finished event !")
        elif request.user.employee.role == 'SUPPORT':
            return obj in Event.objects.filter(
                support_contact=request.user.employee
                )
        elif request.user.employee.role == 'SALES':
            return obj in Event.objects.filter(
                contract__sales_contact=request.user.employee
                )
        else:
            return False
