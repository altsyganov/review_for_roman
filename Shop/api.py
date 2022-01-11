from django.db import models
from rest_framework import decorators
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from .models import Product, Price, Type
from .serializers import ProductSerializer, PriceSerializer, TypeSerializer


# class ProductView(APIView):

#     def get(self, request, pk=None):
#         if pk is None:
#             products = Product.objects.all()
#             serializer = ProductSerializer(products, many=True)
#         else:
#             products = get_object_or_404(Product.objects.all(), pk=pk)
#             serializer = ProductSerializer(products, many=False)
#         return Response({'products': serializer.data})

#     def post(self, request, pk=None):
#         products = request.data.get('products')

#         serializer = ProductSerializer(data=products)
#         if serializer.is_valid(raise_exception=True):
#             products_saved = serializer.save()
#         return Response({'success': f'Product {products_saved.name} created successfully'})

#     def put(self, request, pk):
#         saved_product = get_object_or_404(Product.objects.all(), pk=pk)
#         data = request.data.get('products')
#         serializer = ProductSerializer(instance=saved_product, data=data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             product_saved = serializer.save()
#         return Response({'success': f'Product {product_saved.name} updated successfully'})

#     def delete(self, request, pk):
#         product = get_object_or_404(Product.objects.all(), pk=pk)
#         product.delete()
#         return Response({'message': f'Product with id {pk} has been deleted.'}, status=204)

# class PriceView(APIView):

#     def get(self, request, pk=None):
#         if pk is None:
#             price = Price.objects.all()
#             serializer = PriceSerializer(price, many=True)
#         else:
#             price = get_object_or_404(Price.objects.all(), pk=pk)
#             serializer = PriceSerializer(price, many=False)
#         return Response({'prices': serializer.data})

#     def post(self, request, pk=None):
#         prices = request.data.get('prices')

#         serializer = PriceSerializer(data=prices)
#         if serializer.is_valid(raise_exception=True):
#             prices_saved = serializer.save()
#         return Response({'success': f'Price {prices_saved} created successfully'})

#     def put(self, request, pk):
#         saved_price = get_object_or_404(Price.objects.all(), pk=pk)
#         data = request.data.get('prices')
#         serializer = PriceSerializer(instance=saved_price, data=data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             price_saved = serializer.save()
#         return Response({'success': f'Price {price_saved} updated successfully'})

#     def delete(self, request, pk):
#         price = get_object_or_404(Price.objects.all(), pk=pk)
#         price.delete()
#         return Response({'message': f'Price with id {pk} has been deleted.'}, status=204)


# class TypeView(APIView):
#     def get(self, request, pk=None):
#         if pk is None:
#             type = Type.objects.all()
#             serializer = TypeSerializer(type, many=True)
#         else:
#             type = get_object_or_404(Type.objects.all(), pk=pk)
#             serializer = TypeSerializer(type, many=False)
#         return Response({'types': serializer.data})

#     def post(self, request, pk=None):
#         types = request.data.get('types')

#         serializer = TypeSerializer(data=types)
#         if serializer.is_valid(raise_exception=True):
#             types_saved = serializer.save()
#         return Response({'success': f'Type {types_saved} created successfully'})

#     def put(self, request, pk):
#         saved_type = get_object_or_404(Type.objects.all(), pk=pk)
#         data = request.data.get('types')
#         serializer = TypeSerializer(instance=saved_type, data=data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             type_saved = serializer.save()
#         return Response({'success': f'Type {type_saved} updated successfully'})

#     def delete(self, request, pk):
#         type = get_object_or_404(Type.objects.all(), pk=pk)
#         type.delete()
#         return Response({'message': f'Type with id {pk} has been deleted.'}, status=204)


from rest_framework import viewsets
from rest_framework.decorators import action

from Shop import serializers


class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(methods=['POST'], detail=True)
    def refactor_currency(self, request, pk=None):
        product = self.queryset.get(pk=pk)
        product.count -= 1
        product.save()
        return Response(status=200, data=self.serializer_class(instance=product).data)


class TypeViewSet(viewsets.ModelViewSet):

    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class PriceViewSet(viewsets.ModelViewSet):

    queryset = Price.objects.all()
    serializer_class = PriceSerializer
