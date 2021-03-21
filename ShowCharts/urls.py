from django.urls import path
from ShowCharts import views

urlpatterns = [
    path('',views.home_user, name="home_user" ),
]