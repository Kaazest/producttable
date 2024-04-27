import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')  # Reemplaza 'myproject.settings' con el nombre real de tu módulo de configuración

import django
django.setup()

import random
from django.utils import timezone
from myapp.models import Products  # Asumiendo que el modelo se llama Product en lugar de Products
import datetime

for _ in range(50):
    product = Products(
        esGratuito=random.choice([True, False]),
        fecha_hora=timezone.now(),
        precio=random.uniform(10.00, 1000.00),
        stock=random.randint(1, 100),
        nombre_producto=f"Producto {_ + 1}"
    )
    product.save()