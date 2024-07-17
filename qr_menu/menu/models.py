from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories/')
    link = models.URLField()

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=100)
    info = models.TextField()
    logo = models.ImageField(upload_to='logos/')
    background_image = models.ImageField(upload_to='backgrounds/')

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='menu_items')
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='menu_items/')

    def __str__(self):
        return self.name

