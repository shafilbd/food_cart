from django.urls import path

from . import views

urlpatterns = [
    path('home', views.OfferFoodsList.as_view(), name= 'index'),
    path('lunch_item', views.Lunch_foods.as_view(), name= 'lunch_item'),
    path('dinner_item', views.DinnerIteam.as_view(), name= 'dinner_item')

]
