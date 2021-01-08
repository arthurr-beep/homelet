from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.
@admin.register(models.User)
class CustomAdminUser(UserAdmin):
    """
    Custom User Admin Model

    """

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom User Data",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "issuperhost",
                )
            },
        ),
    )
