from django.urls import path
from .views import customers_list, customer_detail, create_customer

urlpatterns = [
    path('', customers_list),
    path('<int:id>/', customer_detail),
    path('create/', create_customer),
]
