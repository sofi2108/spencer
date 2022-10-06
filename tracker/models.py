from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=255)
    subcategories = models.ManyToManyField('self', blank=True)

class Expense(models.Model):
    amount = models.IntegerField()
    comment = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='categories')
    subcategory = models.ForeignKey(Category, on_delete=models.PROTECT)
    date = models.DateTimeField(default=timezone.now)
