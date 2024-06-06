from django.urls import path
from .views import add_helper, list_helpers, add_customer, list_customers, add_assignment, list_free_helpers

urlpatterns = [
    path('add_helper/', add_helper, name='add_helper'),
    path('list_helpers/', list_helpers, name='list_helpers'),
    path('add_customer/', add_customer, name='add_customer'),
    path('list_customers/', list_customers, name='list_customers'),
    path('add_assignment/', add_assignment, name='add_assignment'),
    path('list_free_helpers/', list_free_helpers, name='list_free_helpers'),
]
