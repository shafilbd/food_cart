from django.urls import path

from . import views

urlpatterns = [
    path('sign-up/', views.SignUpView.as_view(), name='sign-up'),
    path('login/', views.UserLoginView.as_view(), name ='login'),
    path('logout/', views.UserLogoutView.as_view(), name= 'logout'),

]
