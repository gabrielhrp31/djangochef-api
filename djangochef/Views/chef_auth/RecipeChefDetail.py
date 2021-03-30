from datetime import datetime

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from djangochef.serializers.RecipeSerializer import RecipeSerializer

from djangochef.Models.Recipe import Recipe


class RecipeChefDetail(APIView):

    permission_classes = (IsAuthenticated,)

    def put(self, request, pk):
        """
            Update recipes byt needs chef auth for this
        """
        user = request.user
        # confirm that user is logged
        if not user:
            return Response(status=status.HTTP_403_FORBIDDEN)

        # confirm that recipes exists
        recipe_instance = get_object_or_404(Recipe, pk=pk)
        if not recipe_instance:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # confirm that user is recipe owner
        if not user.id == recipe_instance.chef.id:
            return Response(status=status.HTTP_403_FORBIDDEN)
        data = {
            'title': request.data.get('title'),
            'content': request.data.get('content'),
            'chef': request.user.id,
        }
        serializer = RecipeSerializer(instance=recipe_instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
            Delete recipes but needs chef auth for this
        """
        user = request.user
        # confirm that user is logged
        if not user:
            return Response(status=status.HTTP_403_FORBIDDEN)

        recipe_instance = get_object_or_404(Recipe, pk=pk)

        # confirm that user is recipe owner
        if not user.id == recipe_instance.chef.id:
            return Response(status=status.HTTP_403_FORBIDDEN)

        recipe_instance.delete()
        return Response(status=status.HTTP_200_OK)
