from django.db import models

import citext


class TestModel(models.Model):
    text = citext.CITextField()
    char = citext.CICharField(max_length=255)
    email = citext.CIEmailField()
