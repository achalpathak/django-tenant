from django.core.management.commands.migrate import Command as MigrationCommand
from django.db import connection
from ...models import TenantSchemaMap


class Command(MigrationCommand):
    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            schemas = TenantSchemaMap.objects.all()
            for schema in schemas:
                cursor.execute(f"CREATE SCHEMA IF NOT EXISTS {schema.schema_name}")
                cursor.execute(f"SET search_path to {schema.schema_name}")
                super(Command, self).handle(*args, **options)
