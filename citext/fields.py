from django.db.models import CharField, EmailField, TextField
from django.test.utils import ignore_warnings
from django.utils.deprecation import RemovedInDjango51Warning

__all__ = ["CICharField", "CIEmailField", "CIText", "CITextField"]


# RemovedInDjango51Warning.
class CIText:
    def get_internal_type(self):
        return "CI" + super().get_internal_type()

    def db_type(self, connection):
        return "citext"


class CICharField(CIText, CharField):


    def __init__(self, *args, **kwargs):
        with ignore_warnings(category=RemovedInDjango51Warning):
            super().__init__(*args, **kwargs)


class CIEmailField(CIText, EmailField):

    def __init__(self, *args, **kwargs):
        with ignore_warnings(category=RemovedInDjango51Warning):
            super().__init__(*args, **kwargs)


class CITextField(CIText, TextField):

    def __init__(self, *args, **kwargs):
        with ignore_warnings(category=RemovedInDjango51Warning):
            super().__init__(*args, **kwargs)
