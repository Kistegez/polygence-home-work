from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from spending import views

urlpatterns = [
    path('spendings/<ordering>/', views.spending_list),
    path('spendings/', views.add_spending)
]
urlpatterns = format_suffix_patterns(urlpatterns)
