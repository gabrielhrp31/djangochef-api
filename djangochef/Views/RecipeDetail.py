from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from djangochef.Models.Recipe import Recipe
from djangochef.serializers.RecipeSerializer import RecipeSerializer


class RecipeDetail(APIView):

    def get(self, request, pk, *args, **kwargs):
        """
            Registry recipes but needs chef auth login for this
        """
        recipe = Recipe.objects.get(id=pk)
        if recipe:
            serializer = RecipeSerializer(recipe)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)