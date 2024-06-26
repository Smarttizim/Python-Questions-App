import math
from django.db import models
# from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.


class Theme(models.Model):
    image = models.ImageField(upload_to='images')
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class Quest(models.Model): 
    image = models.ImageField(upload_to='images', null=True, blank=True)  # new field
    quest_num = models.IntegerField()
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name="quests")
    question = models.TextField()
    answer = models.TextField(null=True, blank=True)
    input = models.CharField(max_length=500, null=True, blank=True)
    output = models.CharField(max_length=500, null=True,blank=True)

    file = models.FileField(upload_to='files', null=True, blank=True)  # new field

    def __str__(self):
        return f"| {self.theme}"


class Contact(models.Model):
    image = models.ImageField(upload_to='images',null=True, blank=True)
    name = models.CharField(max_length = 300)
    contact = models.IntegerField()
    text = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='files', null=True, blank=True)

    def __str__(self):
        return self.name

    