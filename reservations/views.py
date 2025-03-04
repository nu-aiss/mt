from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Reservation
from customers.models import Customer
from tables.models import Table
import json

def reservation_detail(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    return render(request, "reservations/detail.html", {"reservation": reservation})

def reservations_list(request):
    return render(request, 'reservations/list.html')

def user_reservations(request, user_id):
    reservations = Reservation.objects.filter(customer_id=user_id)
    return render(request, "reservations/user_reservations.html", {"reservations": reservations})

def create_reservation(request):
    if request.method == "POST":
        data = json.loads(request.body)
        customer = get_object_or_404(Customer, id=data["customer_id"])
        table = get_object_or_404(Table, id=data["table_id"])

        # Проверка на наличие брони у клиента в этот день
        if Reservation.objects.filter(customer=customer, date=data["date"]).exists():
            return JsonResponse({"error": "Customer already has a reservation on this day"}, status=400)

        # Проверка на занятость стола
        if Reservation.objects.filter(table=table, date=data["date"]).exists():
            return JsonResponse({"error": "Table is already reserved for this date"}, status=400)

        reservation = Reservation.objects.create(customer=customer, table=table, date=data["date"], status="pending")
        return JsonResponse({"id": reservation.id, "customer": reservation.customer.name, "table": reservation.table.number, "date": reservation.date, "status": reservation.status})

def update_reservation(request, id):
    if request.method == "POST":
        data = json.loads(request.body)
        reservation = get_object_or_404(Reservation, id=id)
        reservation.status = data["status"]
        reservation.save()
        return JsonResponse({"message": "Reservation updated", "status": reservation.status})

def delete_reservation(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    reservation.delete()
    return JsonResponse({"message": "Reservation deleted"})
