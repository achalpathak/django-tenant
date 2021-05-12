from tenant.models import TenantSchemaMap
from django.db import connection
from django.urls import reverse
from django.conf import settings


class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def set_tenant_schema_for_request(self, request):
        if request.path.startswith(reverse("admin:index")):
            with connection.cursor() as cursor:
                cursor.execute(
                    f"SET search_path to {getattr(settings, 'PUBLIC_SCHEMA_NAME', 'public')}"
                )  # setting public schema for admin urls
            return

        hostname = (
            request.get_host().split(":")[0].lower()
        )  # using split to remove port number if present

        subdomain = hostname.split(".")[0]
        schema = TenantSchemaMap.objects.get(subdomain=subdomain)

        with connection.cursor() as cursor:
            cursor.execute(
                f"SET search_path to {schema.schema_name}"
            )  # setting current schema for the request

    def __call__(self, request):
        self.set_tenant_schema_for_request(request)
        response = self.get_response(request)
        return response
