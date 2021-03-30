from django.contrib.auth.base_user import AbstractBaseUser
from djangochef.managers.ChefManager import ChefManager
from django.db import models


class Chef(AbstractBaseUser):
    ADMIN = 'admin'
    STAFF = 'staff'
    STATUS = [
        (ADMIN, 'Admin User'),
        (STAFF, 'Staff User'),
    ]
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    restaurant_name = models.CharField(max_length=50)
    age = models.IntegerField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)  # a admin user; non super-user
    is_admin = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'age', 'restaurant_name']

    objects = ChefManager()

    @staticmethod
    def has_perm(perm, obj=None):
        # "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    @staticmethod
    def has_module_perms(app_label):
        # "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
