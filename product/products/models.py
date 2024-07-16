from django.db import models

# Create your models here.

from django.db import models
from django.contrib import admin


class Product(models.Model):
    ELECTRIC_WIRE_ROPE_HOIST = "Electric Wire Rope Hoist"
    ELECTRIC_CHAIN_HOIST = "Electric Chain Hoist"
    EOT_CRANE = "EOT Crane"
    EOT_CRANE_ACCESSORY = "EOT Crane Accessory"
    CONVEYOR = "Conveyor"

    PRODUCT_CATEGORIES = [
        (ELECTRIC_WIRE_ROPE_HOIST, "Electric Wire Rope Hoist"),
        (ELECTRIC_CHAIN_HOIST, "Electric Chain Hoist"),
        (EOT_CRANE, "EOT Crane"),
        (EOT_CRANE_ACCESSORY, "EOT Crane Accessory"),
        (CONVEYOR, "Conveyor"),
    ]

    name = models.CharField(max_length=255)
    product_type = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=PRODUCT_CATEGORIES)
    speed = models.CharField(max_length=50, blank=True, null=True)
    voltage = models.CharField(max_length=50, blank=True, null=True)
    capacity = models.CharField(max_length=50, blank=True, null=True)
    material_grade = models.CharField(max_length=50, blank=True, null=True)
    frequency = models.CharField(max_length=50, blank=True, null=True)
    automation_grade = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to="products/")

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField()
    contact_number = models.CharField(max_length=20)
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, related_name="inquiries"
    )
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inquiry from {self.name} for {self.product.name if self.product else 'N/A'}"


from django.db import models


class About(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    established_year = models.CharField(max_length=4)
    ceo = models.CharField(max_length=100)
    employees = models.CharField(max_length=50)
    business_nature = models.CharField(max_length=100)
    additional_business = models.CharField(max_length=100)
    turnover = models.CharField(max_length=50)
    banker = models.CharField(max_length=100)
    legal_status = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class AboutUsAdmin(admin.ModelAdmin):
    list_display = ("title", "ceo", "established_year")
    search_fields = ("title", "ceo", "business_nature")
