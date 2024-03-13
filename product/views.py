from rest_framework.views import Response, APIView

from .serializers import ProductListSerializer, StorageListSerializer
from .models import Product, Brand, Category, Image, Storage, Color


class ProductListView(APIView):

    def get(self, request):

        products = Storage.objects.all()

        serializer = StorageListSerializer(products, many=True)

        return Response(serializer.data)
