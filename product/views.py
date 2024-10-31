from rest_framework.views import APIView
from rest_framework import status
from django.http  import Http404
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.db.models import Q
from django.db.models.functions import Lower

"""Passed"""
class ProductsView(APIView):
    def get(self, request):
        obj = Product.objects.all()
        serializers = ProductSerializer(obj, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializers = ProductSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

"""Passed"""
class ProductDetail(APIView):
    def get_by_id(self, id):
        try:
            return Product.objects.get(id=id)
            
        except Product.DoesNotExist:
            raise Http404("Product not found")

    def get(self, request, id):
        obj = self.get_by_id(id)
        serializers = ProductSerializer(obj)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def put(self, request, id, format=None):
        product = self.get_by_id(id=id)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id:str):
        product = Product.objects.get(id=id)
        product.delete()
        return Response({"details": "Product deleted successfully"}, status=status.HTTP_200_OK)

class ProductCount(APIView):
    def get(self, request):
        count = Product.objects.count()
        return Response({"count": count}, status=status.HTTP_200_OK)

# class ProductByCategory(APIView):
#     def get(self, request, category_id:int):
#         obj = Product.objects.filter(category=category_id)
#         serializers = ProductSerializer(obj, many=True)
#         return Response(serializers.data, status=status.HTTP_200_OK)


# class ProductBrand(APIView):
#     def get(self, request, brand_id: int):
#         obj = Product.objects.filter(brand=brand_id)
#         serializers = ProductSerializer(obj, many=True)
#         return Response(serializers.data, status=status.HTTP_200_OK)


class ProductSearch(APIView):
    def post(self, request):
        search_query = request.data.get("query", "")
        if search_query:
            search_results = Product.objects.filter(
                Q(name__icontains=search_query)
                | Q(category__icontains=search_query)
                | Q(brand__icontains=search_query)
                | Q(price__icontains=search_query)
            )
            search_results = search_results.order_by("id")
            serializer = Product(search_results, many=True)
            return Response(serializer.data)
        return Response("Invalid search query", status=status.HTTP_400_BAD_REQUEST)


class CategoryView(APIView):
    def get(self, request):
        obj = Category.objects.all()
        serializers = CategorySerializer(obj, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializers = CategorySerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class BrandView(APIView):
    def get(self, request):
        obj = Brand.objects.all()
        serializers = BrandSerializer(obj, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializers = BrandSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
