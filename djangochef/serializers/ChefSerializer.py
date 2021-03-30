from rest_framework import serializers
from djangochef.Models.Chef import Chef


class ChefSerializer(serializers.ModelSerializer):

    class Meta:

        model = Chef
        password = serializers.CharField(write_only=True)
        token = serializers.CharField(max_length=255, read_only=True)
        extra_kwargs = {'password': {'write_only': True}}
        fields = ['first_name', 'last_name', 'email', 'restaurant_name', 'age', 'password']
