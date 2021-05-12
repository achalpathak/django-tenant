from django.db import models

# Create your models here.


class TenantSchemaMap(models.Model):
    subdomain = models.CharField(max_length=100, unique=True)
    schema_name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)  # to mark the tenant inactive

    def __str__(self):
        return self.subdomain
