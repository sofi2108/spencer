from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryView.as_view(), name='category_list'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('expenses/', views.ExpenseView.as_view()),
    path('expenses/<int:pk>/', views.ExpenseDetailView.as_view())
]