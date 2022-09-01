from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.exceptions import PermissionDenied

from clients.models import Client
from contracts.models import Contract
from events.models import Event


class IsManagement(BasePermission):
    """
    Un membre de l'équipe de gestion peut :
    - Accéder en lecture seule à tous les clients, contrats, événements
      ou employés.
    - La création, modification ou suppression des employés, clients,
      contrats et évènements doit être effectuée via le site d'administration.
    """
    def has_permission(self, request, view):
        return request.user.employee.role == 'MANAGEMENT' and request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)


class ClientPermission(BasePermission):
    """
    Un membre de l'équipe de vente peut :
    - Afficher les informations des clients qui lui sont attribués.
    - Créer des clients.
    - Mettre à jour les informations des clients qui lui sont attribués.

    Un membre de l'équipe de support peut :
    - Afficher les informations des clients liés aux évènements
      qui lui sont attribués.
    """
    def has_permission(self, request, view):
        if request.user.employee.role == 'SUPPORT':
            return request.method in SAFE_METHODS
        return request.user.employee.role == 'SALES'

    def has_object_permission(self, request, view, obj):
        if request.method == 'DELETE':
            return False
        elif request.user.employee.role == 'SUPPORT' and request.method in SAFE_METHODS:
            if obj in Client.objects.filter(contract__event__support_contact=request.user.employee).distinct():
                return True
            return False
        elif request.user.employee.role == 'SALES':
            if obj in Client.objects.filter(sales_contact=request.user.employee):
                return True
            return False
        else:
            return False


class ContractPermision(BasePermission):
    """
    Un membre de l'équipe de vente peut :
    - Afficher les informations des contrats qui lui sont attribués.
    - Créer des contrats pour les clients qui lui sont attribués.
    - Mettre à jour les informations des contrats non signés
      qui lui sont attribués.

    Un membre de l'équipe de support peut :
    - Afficher les informations des contrats liés aux évènements
      qui lui sont attribués.
    """
    def has_permission(self, request, view):
        if request.user.employee.role == 'SUPPORT':
            return request.method in SAFE_METHODS
        return request.user.employee.role == 'SALES'

    def has_object_permission(self, request, view, obj):
        if request.method == 'DELETE':
            return False
        elif request.user.employee.role == 'SUPPORT' and request.method in SAFE_METHODS:
            if obj in Contract.objects.filter(event__support_contact=request.user.employee):
                return True
            return False
        elif request.method in ['PUT', 'PATCH'] and obj.is_signed is True:
            raise PermissionDenied("You cannot update a signed contract !")
        elif request.user.employee.role == 'SALES':
            if obj in Contract.objects.filter(sales_contact=request.user.employee):
                return True
            return False
        else:
            return False


class EventPermission(BasePermission):
    """
    Un membre de l'équipe de vente peut :
    - Créer des évènements pour les contrats signés qui lui sont attribués.
    - Afficher les informations des évènements qu'il a créé.
    - Mettre à jour les informations des évènements non terminés
      qu'il a créé.

    Un membre de l'équipe de support peut :
    - Mettre à jour les informations des évènements non terminés
      qui lui sont attribués.
    """
    def has_permission(self, request, view):
        if request.user.employee.role == 'SUPPORT':
            return request.method in ['GET', 'PUT', 'PATCH']
        return request.user.employee.role == 'SALES'

    def has_object_permission(self, request, view, obj):
        if request.method == 'DELETE':
            return False
        elif request.user.employee.role == 'SUPPORT':
            if obj in Event.objects.filter(support_contact=request.user.employee):
                return True
            return False
        elif request.method in ['PUT', 'PATCH'] and obj.is_finished is True:
            raise PermissionDenied("You cannot update a finished event !")
        elif request.user.employee.role == 'SALES':
            if obj in Event.objects.filter(contract__sales_contact=request.user.employee):
                return True
            return False
        else:
            return False
