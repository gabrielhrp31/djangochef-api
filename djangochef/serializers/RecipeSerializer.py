from rest_framework import serializers
from djangochef.Models.Recipe import Recipe


class RecipeSerializer(serializers.ModelSerializer):

    class Meta:

        model = Recipe
        date = serializers.DateField(read_only=True)
        chef = serializers.ReadOnlyField()
        fields = '__all__'
