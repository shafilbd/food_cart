from django.contrib import admin

# Register your models here.
from all_foods.models import OfferFood
from .models import Food

admin.site.register(Food)
admin.site.register(OfferFood)
