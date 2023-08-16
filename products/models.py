from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} --- {self.pk}"
    
    class Meta:
        db_table = 'categories'


class Brand(models.Model):
    name = models.CharField(max_length=100)
    country  = models.CharField(max_length=30)


    def __str__(self):
        return f"{self.name} - {self.country} --- {self.pk}"

    class Meta:
        db_table = 'brands'


class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.FloatField()
    brand = models.ForeignKey("Brand", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    description = models.TextField()
    weight = models.IntegerField()
    unit = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='products', null=True, blank=True)

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        db_table = 'products'
        ordering = ['-updated', '-created', 'price']