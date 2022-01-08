

from django.core.checks import messages
from django.shortcuts import render
from .models import Product, Blog
from rest_framework.decorators import api_view
from.serializers import ProductSerializer, BlogSerializer
from rest_framework.response import Response
from rest_framework import status, filters, viewsets

# CRUD PRODUCT
'''
@api_view(['GET'])
def allProducts(request):
    products =  Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status= status.HTTP_200_OK )
@api_view(['GET'])
def getProduct(request, id):
    product = Product.objects.get(id=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data, status= status.HTTP_200_OK )
@api_view(['POST'])
def createProduct(request):
    serializer = ProductSerializer(data=request.data, many=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status= status.HTTP_201_CREATED )
@api_view(['POST'])
def updateProduct(request,id):
    product = Product.objects.get(id=id)
    serializer = ProductSerializer(instance = product, data= request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status= status.HTTP_202_ACCEPTED)
@api_view(['DELETE'])
def delProduct(request,id):
    product = Product.objects.get(id=id)
    product.delete()
    return Response("Product is deleted !", status= status.HTTP_200_OK)

# viesets
class Product_crud(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class Blog_crud(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    '''
@api_view(['GET', 'POST'])
def product_CR(request):
    if request.method == "POST":
        prod = Product()
        prod.title = request.POST.get('title')
        prod.description = request.POST.get('description')
        prod.date_Add= request.POST.get('date_add')
        
        if len(request.FILES) !=0:
            prod.image = request.FILES['image']

        prod.save()
        messages.success(request, "Product added Successfully")
        return Response(status= status.HTTP_201_CREATED)
        #POST
    elif request.method == 'GET': 
        products =  Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK )


@api_view(['GET', 'PUT', 'DELETE'])
def prodcut_rud(request, id):
    try :
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        product.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
    


