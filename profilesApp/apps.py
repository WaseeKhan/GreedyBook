from django.apps import AppConfig


class ProfilesappConfig(AppConfig):
    # default_auto_field = 'django.db.models.BigAutoField'
    name = 'profilesApp'

    def ready(self):
        import profilesApp.signals