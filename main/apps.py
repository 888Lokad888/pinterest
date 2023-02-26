from django.apps import AppConfig

class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    verbose_name = 'Приложение Main'
    name = 'main'

    def ready(self):
        import main.signals