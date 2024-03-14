from rest_framework import status
from rest_framework.views import APIView, Response

from .serializers import UserCreateSerializer, UserListSerializer, ProfileListSerializer, ProfileUpdateSerializer
from .models import MyUser


class UserCreateView(APIView):

    def get(self, request):
        users = MyUser.objects.all()

        serializer = UserListSerializer(users, many=True)

        return Response(serializer.data)

    def post(self, request):

        serializer = UserCreateSerializer(data=request.data, context={'request': request})

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(status.HTTP_400_BAD_REQUEST)


class ProfileListView(APIView):

    def get(self, request):
        user = MyUser.objects.get(id=request.user.id)

        serializer = ProfileListSerializer(user)

        return Response(serializer.data)

    def patch(self, request):
        user = MyUser.objects.get(id=request.user.id)
        serializer = ProfileUpdateSerializer(instance=user, data=request.data, partial=True,
                                             context={'request': request})

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
