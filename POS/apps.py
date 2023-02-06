from django.apps import AppConfig


class PosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'POS'
    def ready(self):
            from scheduler import scheduler
            scheduler.start()
