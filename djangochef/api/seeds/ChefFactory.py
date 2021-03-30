import factory
from faker import Factory

from djangochef.Models.Chef import Chef

faker = Factory.create()


class ChefFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Chef

    def __init__(self, chef_id) -> None:
        self.chef_id = chef_id

    first_name = faker.first_name()
    last_name = faker.last_name()
    email = faker.email()
    restaurant_name = faker.company()
    age = faker.random_int()
    is_active = True
    is_staff = False
    is_admin = False
    password = factory.PostGenerationMethodCall(
        'set_password',
        faker.password(
            length=10,
            special_chars=True,
            digits=True,
            upper_case=True,
            lower_case=True,
        )
    )