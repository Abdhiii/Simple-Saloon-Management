from django.urls import path
from .views import home, generate_ticket

urlpatterns = [
    path('', home, name="home"),
    path('generate-ticket/', generate_ticket, name="generate_ticket"),
]
