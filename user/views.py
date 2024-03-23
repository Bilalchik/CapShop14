from rest_framework import status
from rest_framework.views import APIView, Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializers import UserCreateSerializer, UserListSerializer, ProfileListSerializer, ProfileUpdateSerializer
from .models import MyUser


class UserCreateView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('username', openapi.IN_QUERY, description="Широта центра области",
                              type=openapi.TYPE_NUMBER, required=True),
            openapi.Parameter('center_lon', openapi.IN_QUERY, description="Долгота центра области",
                              type=openapi.TYPE_NUMBER, required=True),
            openapi.Parameter('radius', openapi.IN_QUERY, description="Радиус области (в километрах)",
                              type=openapi.TYPE_NUMBER, required=True),
        ],
        responses={
            200: openapi.Response('200 OK', UserListSerializer()),
        }
    )
    def get(self, request):
        users = MyUser.objects.all()

        serializer = UserListSerializer(users, many=True)

        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=UserCreateSerializer()
    )
    def post(self, request):

        serializer = UserCreateSerializer(data=request.data, context={'request': request})

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(status.HTTP_400_BAD_REQUEST)


class ProfileListView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('username', openapi.IN_QUERY, description="Широта центра области", type=openapi.TYPE_NUMBER, required=True),
            openapi.Parameter('center_lon', openapi.IN_QUERY, description="Долгота центра области", type=openapi.TYPE_NUMBER, required=True),
            openapi.Parameter('radius', openapi.IN_QUERY, description="Радиус области (в километрах)", type=openapi.TYPE_NUMBER, required=True),
        ],
        responses={
            200: openapi.Response('200 OK', ProfileListSerializer()),
        }
    )
    def get(self, request):
        user = MyUser.objects.get(id=request.user.id)

        serializer = ProfileListSerializer(user)

        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=ProfileUpdateSerializer()
    )
    def patch(self, request):
        user = MyUser.objects.get(id=request.user.id)
        serializer = ProfileUpdateSerializer(instance=user, data=request.data, partial=True,
                                             context={'request': request})

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
