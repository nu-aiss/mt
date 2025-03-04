from django.shortcuts import render
from django.http import JsonResponse
from .models import Table
import json

def tables_list(request):
    tables = Table.objects.all()
    return render(request, "tables/list.html", {"tables": tables})

def available_tables(request):
    available_tables = Table.objects.filter(is_available=True)
    return render(request, "tables/available.html", {"tables": available_tables})

def create_table(request):
    if request.method == "POST":
        data = json.loads(request.body)
        table = Table.objects.create(number=data["number"], seats=data["seats"])
        return JsonResponse({"id": table.id, "number": table.number, "seats": table.seats, "is_available": table.is_available})

