from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from djangochef.serializers.ChefSerializer import ChefSerializer


class ChefCreate(APIView):

    def post(self, request, *args, **kwargs):
        """
            Chef user creation is required to create recipes
        """
        data = {
            'email': request.data.get('email'),
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name'),
            'restaurant_name': request.data.get('restaurant_name'),
            'age': request.data.get('age'),
            'password': request.data.get('password'),
        }
        serializer = ChefSerializer(data=data)
        if serializer.is_valid():
            # encode user password for security and the same work
            data['password'] = make_password(data['password'])
            serializer = ChefSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)