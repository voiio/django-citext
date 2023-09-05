from django.contrib.postgres.operations import CreateExtension


class CITextExtension(CreateExtension):
    def __init__(self):
        self.name = "citext"
