from django.contrib.postgres.operations import CreateExtension

__all__ = ["CITextExtension"]


class CITextExtension(CreateExtension):
    def __init__(self):
        self.name = "citext"
