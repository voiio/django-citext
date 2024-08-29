from django.apps import AppConfig


class CITextAppConfig(AppConfig):
    name = "citext"

    def ready(self):
        from citext import baker_generators  # noqa
