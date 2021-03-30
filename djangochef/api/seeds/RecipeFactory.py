import factory
from faker import Factory

from djangochef.Models.Chef import Chef
from djangochef.Models.Recipe import Recipe

faker = Factory.create()


class RecipeFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Recipe

    title = faker.sentence(nb_words=4)
    content = faker.paragraph(nb_sentences=5)