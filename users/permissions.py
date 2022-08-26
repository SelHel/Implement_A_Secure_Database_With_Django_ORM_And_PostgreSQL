from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.exceptions import PermissionDenied


class ClientPermission(BasePermission):
    """
    Un membre de l'équipe de gestion peut :
    - Afficher les informations de tous les clients
    Un membre de l'équipe de vente peut :
    - Créer des clients.
    - Mettre à jour les informations des clients qui lui sont attribués.

    Un membre de l'équipe de support peut :
    - Afficher les informations des clients liés aux évènements
      qui lui sont attribués.
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
            return obj.sales_contact.user == request.user.employee


class ContractPermision(BasePermission):
    """
    Un membre de l'équipe de vente peut :
    - Créer des contrats pour les clients qui lui sont attribués.
    - Mettre à jour les informations des contrats non signés
      qui lui sont attribués.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.employee.role == 'SALES'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.method == 'DELETE':
            return False
        elif obj.is_signed is True:
            raise PermissionDenied("You cannot update a signed contract !")
        else:
            return obj.sales_contact.user == request.user.employee


class EventPermission(BasePermission):
    """
    Un membre de l'équipe de vente peut :
    - Créer des évènements pour les contrats qui lui sont attribués.
    - Mettre à jour les informations des évènements non terminés
      qui lui sont attribués.

    Un membre de l'équipe de support peut :
    - Mettre à jour les informations des évènements non terminés
      qui lui sont attribués.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.employee.role == 'SALES'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.method == 'DELETE':
            return False
        elif obj.is_finished is True:
            raise PermissionDenied("You cannot update a finished event !")
        else:
            check = (
                obj.support_contact.user == request.user.employee
                ) or (
                    obj.contract.sales_contact.user == request.user.employee
                    )
            return check
