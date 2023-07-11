from django.apps import AppConfig


class OhmsAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "ohms_app"

    def ready(self):
        import ohms_app.signals
