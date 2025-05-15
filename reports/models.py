import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _


class Report(models.Model):
    class Type(models.TextChoices):
        SALES = 'sales', _('Sales')
        PRODUCTS = 'products', _('Products')
        USERS = 'users', _('Users')
        CUSTOM = 'custom', _('Custom')
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=Type.choices)
    parameters = models.JSONField()
    file = models.FileField(upload_to='reports/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_ready = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name


class Dashboard(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    configuration = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name