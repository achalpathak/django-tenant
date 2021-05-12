from django.conf import settings
from django.apps import apps as django_apps


class TenantSyncRouter(object):
    def app_in_list(self, app_label, apps_list):
        appconfig = django_apps.get_app_config(app_label)
        appconfig_full_name = "{}.{}".format(
            appconfig.__module__, appconfig.__class__.__name__
        )
        return (appconfig.name in apps_list) or (appconfig_full_name in apps_list)

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        from django.db import connection

        with connection.cursor() as cursor:
            cursor.execute("show search_path")
            schema_name = cursor.fetchone()[0]

        try:
            schema_name = schema_name.split(",")[
                1
            ].strip()  # will set the schema for public
        except Exception as e:
            pass  # will set the schema for tenants

        if schema_name == getattr(settings, "PUBLIC_SCHEMA_NAME", "public"):
            if not self.app_in_list(app_label, settings.SHARED_APPS):
                return False
        else:
            if not self.app_in_list(app_label, settings.TENANT_APPS):
                return False

        return None
