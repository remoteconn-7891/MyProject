from django.apps import AppConfig

class ArborfindrConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'arborfindr'

    def ready(self):
        import arborfindr.signals
