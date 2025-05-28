from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class FoodItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    calories = models.PositiveIntegerField()
    date_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.name} - {self.calories} cal"
    
    class Meta:
        ordering = ['-date_added']