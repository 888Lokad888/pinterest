from django.apps import AppConfig

class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    verbose_name = 'Главная страница'
    name = 'main'

    def ready(self):
        import main.signals