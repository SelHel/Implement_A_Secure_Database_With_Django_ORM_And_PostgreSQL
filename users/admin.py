from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from users.models import Employee


class EmployeeInline(admin.StackedInline):
    model = Employee


class EmployeeAdmin(UserAdmin):
    @staticmethod
    def role(obj):
        return obj.employee.role

    @staticmethod
    def is_staff(obj):
        return obj.is_staff

    @staticmethod
    def is_superuser(obj):
        return obj.is_superuser

    inlines = (EmployeeInline, )
    list_display = (
        'id',
        'username',
        'first_name',
        'last_name',
        'role',
        'is_staff',
        'is_superuser'
        )

    add_fieldsets = [
        (
            'Credentials',
            {
                'fields': ['username', 'password1', 'password2']
            }
        ),
        (
            'Personal info',
            {
                'classes': ('wide',),
                'fields': ['first_name', 'last_name', 'email'],
                'description': 'This contains the personal info'
            }
        )
    ]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if hasattr(obj, 'employee') and obj.employee.role == 'MANAGEMENT':
            obj.is_staff = True
            obj.is_superuser = True
            obj.save()


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User, EmployeeAdmin)
