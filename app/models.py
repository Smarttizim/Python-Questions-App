import math
from django.db import models

# Create your models here.


class Theme(models.Model):
    image = models.ImageField(upload_to='images')
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class Quest(models.Model):
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name ="themes")
    question = models.TextField()
    answer = models.TextField(null=True, blank=True)
    one_id = models.IntegerField(null=True, blank=True, unique=True, default=0)
    
    @property
    def one_id(self):  # noqa
        return 0 + self.id
    
    def __str__(self):
        return f"| {self.theme}"

    