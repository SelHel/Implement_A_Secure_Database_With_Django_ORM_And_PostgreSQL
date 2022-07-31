from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from users.models import Employee


class EmployeeInline(admin.StackedInline):
    model = Employee


class EmployeeAdmin(UserAdmin):
    inlines = (EmployeeInline, )


admin.site.unregister(User)
admin.site.register(User, EmployeeAdmin)
