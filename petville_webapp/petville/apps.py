from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'petville'

    def ready(self):
        import petville.signals  # noqa
