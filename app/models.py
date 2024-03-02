import math
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.


class Theme(models.Model):
    image = models.ImageField(upload_to='images')
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class Quest(models.Model):
    quest_num = models.IntegerField()
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name ="themes")
    question = CKEditor5Field('Text', config_name='extends')
    answer = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"| {self.theme}"

    