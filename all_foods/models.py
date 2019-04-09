from django.db import models

# Create your models here.
from all_foods.constants import FOODS_TYPE


class Food(models.Model):
    name = models.CharField(max_length=25, verbose_name='foods Name :')
    type = models.CharField(max_length=30, verbose_name='foods type :', choices=FOODS_TYPE)
    article = models.CharField(max_length=250, verbose_name= 'food article :')
    image = models.FileField()
    price = models.IntegerField(default=0000,verbose_name='current_price')

    def __str__(self):
        return '{foods_name}'.format(foods_name = self.name)

class OfferFood(models.Model):
    all_food = models.ForeignKey(Food,on_delete=models.CASCADE)
    Offer_price = models.IntegerField(default=0000,verbose_name='Offer_price')

    def __str__(self):
        return '{offer_food_name}'.format(offer_food_name = self.all_food.name)

