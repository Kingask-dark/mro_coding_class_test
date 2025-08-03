from django.apps import AppConfig


class ModelSignalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'model_signal'
    
    def ready(self):
        import model_signal.signals
