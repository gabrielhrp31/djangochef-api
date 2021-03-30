from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from djangochef.Models.Recipe import Recipe
from djangochef.serializers.RecipeSerializer import RecipeSerializer


class RecipeFilter(APIView):

    def get(self, request):
        """
            Return recipes that's contains data in title or content
        """
        data = request.GET['data']
        # verify if user passed data to search by recipes
        if not data:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        recipe = Recipe.objects.filter(Q(title__contains=data) or Q(content__contains=data))
        if recipe:
            serializer = RecipeSerializer(recipe, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)