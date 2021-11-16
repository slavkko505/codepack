from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from . import permissions
from .serializers import JewelryListSerializer
from .models import Jewelry
from .permissions import ReadOnlyOrAdmin
from rest_framework.permissions import IsAdminUser
from constants import  *

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/jewelry-list/',
        'Detail View': '/jewelry-detail/<int:id>/',
        'Create': '/jewelry-create/',
        'Update': '/jewelry-update/<int:id>/',
        'Delete': '/jewelry-detail/<int:id>/',
    }
    return Response(api_urls);


class PageNumberAsLimitOffset(PageNumberPagination):
    page_query_param = "offset"
    page_size_query_param = "limit"
    page_size = page_size_value
    max_page_size = max_page_size_value


@api_view(['GET'])
def ShowAll(request):
    def get_permissions(self):
        if self.request.method == 'GET' or self.request.method == 'PUT' or self.request.method == 'DELETE':
            return (permissions.IsAuthenticated(), IsAdminUser(),)
    products = Jewelry.objects.all()
    paginator = PageNumberAsLimitOffset()
    result_page = paginator.paginate_queryset(products, request)
    serializer = JewelryListSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)



@api_view(['GET'])
def ViewProduct(request, pk):
    def get_permissions(self):
        if self.request.method == 'GET' or self.request.method == 'PUT' or self.request.method == 'DELETE':
            return (permissions.IsAuthenticated(), IsAdminUser(),)
    product = Jewelry.objects.get(id=pk)
    serializer = JewelryListSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def CreateProduct(request):
    def get_permissions(self):
        if self.request.method == 'GET' or self.request.method == 'PUT' or self.request.method == 'DELETE':
            return (permissions.IsAuthenticated(), IsAdminUser(),)
    serializer = JewelryListSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



@api_view(['POST'])
def updateProduct(request, pk):
    def get_permissions(self):
        if self.request.method == 'GET' or self.request.method == 'PUT' or self.request.method == 'DELETE':
            return (permissions.IsAuthenticated(), IsAdminUser(),)
    product = Jewelry.objects.get(id=pk)
    serializer = JewelryListSerializer(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def deleteProduct(request, pk):
    def get_permissions(self):
        if self.request.method == 'GET' or self.request.method == 'PUT' or self.request.method == 'DELETE':
            return (permissions.IsAuthenticated(), IsAdminUser(),)
    product = Jewelry.objects.get(id=pk)
    product.delete()

    return Response('Items delete successfully!')



