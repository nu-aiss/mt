from django.urls import path
from .views import tables_list, available_tables, create_table

urlpatterns = [
    path('', tables_list),
    path('available/', available_tables),
    path('create/', create_table),
]
