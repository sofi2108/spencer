from email.policy import default
from django.shortcuts import get_object_or_404

from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models
from . import serializers


class CategoryView(APIView):
    def get(self, request):
        queryset = models.Category.objects.all()
        serializer = serializers.CategorySerializer(queryset, many=True)

        return Response(serializer.data)
    
    def post(self, request):
        serializer = serializers.CategorySerializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

class CategoryDetailView(APIView):
    def get(self, request, pk):
        category = get_object_or_404(models.Category, pk=pk)
        serializer = serializers.CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk):
        category = get_object_or_404(models.Category, pk=pk)
        serializer = serializers.CategorySerializer(category, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, pk):
        category = get_object_or_404(models.Category, pk=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ExpenseView(APIView):

    def get(self, request):

        serializer = serializers.ExpensesParamSerializer(data= request.GET)

        if 'size' in request.GET:
            size = self.request.query_params['size']
        else:
            size = 20

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        filter_params = {key : value for key, value in serializer.data.items() if value is not None}

        expenses = models.Expense.objects.filter(**filter_params).order_by('date')[:size]
        
        expense_serializer = serializers.ExpensesSerializer(expenses, many=True)

        return Response(expense_serializer.data)

    def post(self, request):
        serializer = serializers.ExpensesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

class ExpenseDetailView(APIView):
    def get(self, request, pk):
        Expense = get_object_or_404(models.Expense, pk=pk)
        serializer = serializers.ExpensesSerializer(Expense)
        return Response(serializer.data)

    def put(self, request, pk):
        expense = get_object_or_404(models.Expense, pk=pk)
        serializer = serializers.ExpensesSerializer(expense, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, pk):
        expense = get_object_or_404(models.Expense, pk=pk)
        expense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






