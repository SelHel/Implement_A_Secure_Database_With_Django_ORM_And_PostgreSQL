from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.exceptions import PermissionDenied


class ClientPermission(BasePermission):
    """
    Les utilisateurs authentifiés ont un accès en lecture seule
    à tous les clients.
    Un membre de l'équipe de vente peut :
    - Créer des clients.
    - Mettre à jour les informations des clients qui lui sont attribués.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.employee.role == 'SALES'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        elif request.method == 'DELETE':
            return False
        else:
            return obj.sales_contact.user == request.user


class ContractPermision(BasePermission):
    """
    Les utilisateurs authentifiés ont un accès en lecture seule
    à tous les contrats.
    Un membre de l'équipe de vente peut :
    - Créer des contrats.
    - Mettre à jour les informations des contrats qui lui sont attribués.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.employee.role == 'SALES'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        elif request.method == 'DELETE':
            return False
        elif obj.is_signed is True:
            raise PermissionDenied("You cannot update a signed contract !")
        else:
            return obj.sales_contact.user == request.user


class EventPermission(BasePermission):
    """
    Les utilisateurs authentifiés ont un accès en lecture seule
    à tous les évènements.
    Un membre de l'équipe de vente peut :
    - Créer des évènements.
    - Mettre à jour les informations des évènements qui lui sont attribués.
    Un membre de l'équipe de support peut :
    - Mettre à jour les informations des évènements qui lui sont attribués.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if request.method == 'PUT':
            return request.user.employee.role == 'SUPPORT'
        return request.user.employee.role == 'SALES'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        elif request.method == 'DELETE':
            return False
        elif obj.is_finished is True:
            raise PermissionDenied("You cannot update a finished event !")
        else:
            return obj.support_contact.user == request.user or obj.contract.sales_contact.user == request.user
