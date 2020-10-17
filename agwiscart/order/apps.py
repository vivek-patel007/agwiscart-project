from django.apps import AppConfig


class OrderConfig(AppConfig):
    name = 'order'

    def ready(self):
        # import signal handlers
        import agwiscart.signal