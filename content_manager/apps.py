from django.apps import AppConfig


class ContentManagerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'content_manager'

    def ready(self):
        import content_manager.signals  # noqa
