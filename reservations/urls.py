from django.urls import path
from .views import (
    reservations_list,  
    reservation_detail,  
    user_reservations,  
    create_reservation,  
    update_reservation,  
    delete_reservation   
)

urlpatterns = [
    path('', reservations_list, name='reservations_list'),
    path('<int:id>/', reservation_detail, name='reservation_detail'),
    path('user/<int:user_id>/', user_reservations, name='user_reservations'),
    path('create/', create_reservation, name='create_reservation'),
    path('<int:id>/update/', update_reservation, name='update_reservation'),
    path('<int:id>/delete/', delete_reservation, name='delete_reservation'),
]

