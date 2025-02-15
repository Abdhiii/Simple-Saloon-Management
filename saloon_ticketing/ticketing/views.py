from django.shortcuts import render
from django.http import JsonResponse
import random
import json
from .models import Ticket

# Service Prices
SERVICES = {
    "Hair Cut": 300,
    "Spa": 500,
    "Facial": 350,
}

def home(request):
    return render(request, "ticketing/index.html")

def generate_ticket(request):
    if request.method == "POST":
        try:
            # Parse JSON data from request
            data = json.loads(request.body.decode("utf-8"))
            customer_name = data.get("customer_name")
            selected_services = data.get("services", [])

            if not customer_name or not selected_services:
                return JsonResponse({"error": "Missing customer name or services"}, status=400)

            # Generate ticket ID
            ticket_id = f"T-{random.randint(1000, 9999)}"

            # Calculate total amount
            total_amount = sum(SERVICES.get(service, 0) for service in selected_services)

            # Save to database
            ticket = Ticket.objects.create(
                ticket_id=ticket_id,
                customer_name=customer_name,
                services=", ".join(selected_services),  # Convert list to string
                total_amount=total_amount
            )

            return JsonResponse({
                "ticket_id": ticket.ticket_id,
                "customer_name": ticket.customer_name,
                "services": selected_services,
                "total_amount": ticket.total_amount
            })

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request"}, status=400)
