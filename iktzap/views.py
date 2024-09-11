from django.shortcuts import render
from rest_framework import generics, viewsets 
from rest_framework.response import Response

from .models import Category
from .serializers import CategorySerializer



# Create your views here.
class CategoryAPIViewSets(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'category_id'
    
    # def get_queryset(self):
    #     # Получение параметра category_id из URL
    #     category_id = self.request.query_params.get('category_id', None)
    #     if category_id is not None:
    #         # Фильтрация по category_id
    #         return self.queryset.filter(category_id=category_id)
    #     return super().get_queryset()