from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    created_at =  models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Farmer_Hand.Category', blank= True, null=True, on_delete=models.PROTECT,related_name='posts')

    def __str__(self):
        return self.title
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

