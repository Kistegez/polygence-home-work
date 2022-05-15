from django.urls import path
from spending import views

urlpatterns = [
    path('spendings/', views.spending_list),
]