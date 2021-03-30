from django.contrib.auth.base_user import BaseUserManager


def validate(email, first_name, restaurant_name, age, last_name, password=None):
    if not email:
        raise ValueError("User must have an email")
    if not restaurant_name:
        raise ValueError("User must specify a restaurant or say its cook in home")
    if not age:
        raise ValueError("User must specify an age")
    if not password:
        raise ValueError("User must have a password")
    if not first_name:
        raise ValueError("User must have a first name")
    if not last_name:
        raise ValueError("User must have a last name")


class ChefManager(BaseUserManager):
    def create_user(self, email, restaurant_name, age, first_name, last_name, password=None):
        validate(email, restaurant_name, age, first_name, last_name, password)
        user = self.model(
            email=self.normalize_email(email)
        )
        user.first_name = first_name
        user.last_name = last_name
        user.restaurant_name = restaurant_name
        user.age = age
        user.set_password(password)  # change password to hash
        user.is_admin = False
        user.is_staff = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, restaurant_name, age, first_name, last_name, password=None):
        validate(email, restaurant_name, age, first_name, last_name, password)
        user = self.model(
            email=self.normalize_email(email)
        )
        user.first_name = first_name
        user.last_name = last_name
        user.restaurant_name = restaurant_name
        user.age = age
        user.set_password(password)  # change password to hash
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, restaurant_name, age, first_name, last_name,  password=None):
        validate(email, restaurant_name, age, first_name, last_name, password)
        user = self.model(
            email=self.normalize_email(email)
        )
        user.first_name = first_name
        user.last_name = last_name
        user.restaurant_name = restaurant_name
        user.age = age
        user.set_password(password)  # change password to hash
        user.is_admin = False
        user.is_staff = True
        user.save(using=self._db)
        return user
