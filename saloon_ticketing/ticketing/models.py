from django.db import models

from django.db import models

class Ticket(models.Model):
    ticket_id = models.CharField(max_length=20, unique=True)
    customer_name = models.CharField(max_length=255)
    services = models.JSONField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)  # No default needed

    def __str__(self):
        return f"{self.ticket_id} - {self.customer_name}"