from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'


    def ready(self):    # Adding the signals to the User's app
        import users.signals
