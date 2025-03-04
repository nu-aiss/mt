from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Customer
import json

def customers_list(request):
    customers = Customer.objects.all()
    return render(request, "customers/list.html", {"customers": customers})

def customer_detail(request, id):
    customer = get_object_or_404(Customer, id=id)
    return render(request, "customers/detail.html", {"customer": customer})

def create_customer(request):
    if request.method == "POST":
        data = json.loads(request.body)
        customer = Customer.objects.create(name=data["name"], phone=data["phone"])
        return JsonResponse({"id": customer.id, "name": customer.name, "phone": customer.phone})
