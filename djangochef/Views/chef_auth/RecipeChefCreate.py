from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from djangochef.serializers.RecipeSerializer import RecipeSerializer


class RecipeChefCreate(APIView):

    permission_classes = (IsAuthenticated,)

    def post(self, request):
        """
            Create recipes but requires chef auth for this
        """
        user = request.user
        # confirm that user is logged
        if not user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        data = {
            'title': request.data.get('title'),
            'content': request.data.get('content'),
            'chef': request.user.id,
        }
        serializer = RecipeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)