from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from spending import views

urlpatterns = [
    path('spendings/', views.spending_list),
    path('spendings/<filter>/', views.spending_list_filter),
]
urlpatterns = format_suffix_patterns(urlpatterns)
