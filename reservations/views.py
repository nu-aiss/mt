from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Reservation
from customers.models import Customer
from tables.models import Table
import json
from .forms import ReservationForm


def reservation_detail(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    return render(request, "reservations/detail.html", {"reservation": reservation})

def reservations_list(request):
    reservations = Reservation.objects.all()
    return render(request, "reservations/list.html", {"reservations": reservations})

def user_reservations(request, user_id):
    reservations = Reservation.objects.filter(user_id=user_id)
    return render(request, "reservations/user_reservations.html", {"reservations": reservations})

def create_reservation(request):
    if request.method == "POST":
        customer_id = request.POST.get("customer_id")  
        table_id = request.POST.get("table_id")
        date = request.POST.get("date")

        customer = get_object_or_404(Customer, id=customer_id)
        table = get_object_or_404(Table, id=table_id)

        reservation = Reservation.objects.create(
            customer=customer,
            table=table,
            date=date,
            status="pending"
        )
        reservation.save()

        return redirect("reservations_list")

    customers = Customer.objects.all()
    tables = Table.objects.all()
    return render(request, "reservations/create.html", {"customers": customers, "tables": tables})

def update_reservation(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    
    if request.method == "POST":
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect("reservations_list")
        else:
            return JsonResponse({"error": "Invalid form submission"}, status=400)
    
    form = ReservationForm(instance=reservation)
    return render(request, "reservations/update.html", {"form": form})

def delete_reservation(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    reservation.delete()
    return redirect("reservations_list")
