from rest_framework import serializers
from .models import Category, Expense


class ExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ExpensesParamSerializer(serializers.Serializer):
    date__gte = serializers.DateTimeField(required=False)
    date__lte = serializers.DateTimeField(required=False)


