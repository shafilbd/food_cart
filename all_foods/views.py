from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, TemplateView, View

from .models import OfferFood, Food


#@method_decorator(login_required, name='dispatch')
class OfferFoodsList(ListView):
    model = OfferFood
    template_name = 'index.html'


    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.select_related('all_food')

@method_decorator(login_required, name='dispatch')
class Lunch_foods(ListView):
    model = Food
    template_name = 'Lunch_iteam.html'
    queryset = Food.objects.all()
    lunch_item = Food.objects.filter(type ='Lunch')
    context_object_name = 'luch'

    def get_context_data(self, **kwargs):
        lunch = super().get_context_data(**kwargs)
        lunch['lunch_item'] = self.lunch_item[:10]
        return lunch

@method_decorator(login_required, name='dispatch')
class DinnerIteam(ListView):
    model = Food
    template_name = 'dinner_items.html'
    queryset = Food.objects.all()
    dinner_item = Food.objects.filter(type = 'Dinner')
    context_object_name = 'dinners'

    def get_context_data(self, **kwargs):
        dinner = super().get_context_data(**kwargs)
        dinner['dinner_item'] = self.dinner_item[:10]
        return dinner

