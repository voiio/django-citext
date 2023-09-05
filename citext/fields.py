from django.db import models

__all__ = ["CICharField", "CIEmailField", "CIText", "CITextField"]


class CIText:
    def get_internal_type(self):
        return "CI" + super().get_internal_type()

    def db_type(self, connection):
        return "citext"


class CICharField(CIText, models.CharField):
    pass


class CIEmailField(CIText, models.EmailField):
    pass


class CITextField(CIText, models.TextField):
    pass
