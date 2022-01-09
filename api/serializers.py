from rest_framework import serializers
from .models import Blog, Product

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model= Blog
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields = '__all__'
'''
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ['id', 'name','email', 'password']
        '''