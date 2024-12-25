from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Service(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField(null=True,blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    counts=models.PositiveIntegerField
    image=models.ImageField(upload_to='servises/')
    def __str__(self):
        return self.name
