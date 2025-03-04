from django.urls import path
from .views import reservation_detail, user_reservations, create_reservation, update_reservation, delete_reservation

urlpatterns = [
    path('<int:id>/', reservation_detail),
    path('user/<int:user_id>/', user_reservations),
    path('create/', create_reservation),
    path('<int:id>/update/', update_reservation),
    path('<int:id>/delete/', delete_reservation),
]
