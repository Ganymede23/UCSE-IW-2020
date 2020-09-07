from django.apps import AppConfig

class UsuarioConfig(AppConfig):
    name = 'usuario'

    def ready(self):
        import usuario.signals
