from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from djangochef.Models.Chef import Chef
from djangochef.serializers.RecipeSerializer import RecipeSerializer


class RecipesListChef(APIView):

    def get(self, request, pk, *args, **kwargs):
        """
            List all recipes from a specified id chef
        """
        chef = Chef.objects.get(id=pk)
        if chef:
            serializer = RecipeSerializer(chef.recipe_set, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)