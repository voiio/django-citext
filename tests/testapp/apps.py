from django.apps import AppConfig


class TestAppConfig(AppConfig):
    name = "tests.testapp"

    def ready(self):
        from citext import baker_generators  # noqa
