from django.db import models

from . import lookups

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


field: models.Field

for field in CIText.__subclasses__():
    for lookup in lookups.CompareCITextLookupMixin.__subclasses__():
        field.register_lookup(lookup)

    for lookup in lookups.InsensitiveCompareCITextLookupMixin.__subclasses__():
        field.register_lookup(lookup)

    field.register_lookup(lookups.IsNull)


from . import baker_generators  # noqa
