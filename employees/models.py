import uuid
from django.db import models

class Employee(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    company_name = models.CharField(max_length=255)
    role_name = models.CharField(max_length=100)
    linkedin_profile = models.URLField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    email=models.EmailField(unique=True,default="examle@gmail.com")

    def __str__(self):
        return f"{self.first_name} - {self.company_name}"
