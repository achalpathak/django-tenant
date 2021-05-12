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
        from django.db import connection, DEFAULT_DB_ALIAS

        if db != getattr(settings, "TENANT_DB_ALIAS", DEFAULT_DB_ALIAS):
            return False

        # connection = connections[db]
        with connection.cursor() as cursor:
            cursor.execute("show search_path")
            try:
                schema_name = cursor.fetchone()[0].split(",")[1].strip()
            except Exception as e:
                schema_name = cursor.fetchone()[0]
        if schema_name == getattr(settings, "PUBLIC_SCHEMA_NAME", "public"):
            if not self.app_in_list(app_label, settings.SHARED_APPS):
                return False
        else:
            if not self.app_in_list(app_label, settings.TENANT_APPS):
                return False

        return None
