import math
from django.db import models

# Create your models here.


class Theme(models.Model):
    image = models.ImageField(upload_to='images')
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class Quest(models.Model):
    quest_num = models.IntegerField()
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name ="themes")
    question = models.TextField()
    answer = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"| {self.theme}"

    