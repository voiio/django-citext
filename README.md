# Django CITEXT

PostgreSQL CITEXT integration for Django.

[![PyPi Version](https://img.shields.io/pypi/v/citext.svg)](https://pypi.python.org/pypi/citext/)
[![Test Coverage](https://codecov.io/gh/voiio/citext/branch/main/graph/badge.svg)](https://codecov.io/gh/voiio/citext)
[![GitHub License](https://img.shields.io/github/license/voiio/citext)](https://raw.githubusercontent.com/voiio/citext/master/LICENSE)

## Setup

```ShellSession
python3 -m pip install django-citext
```

```python
# settings.py
INSTALLED_APPS = [
    'citext',
    # ...
]
```

## Usage

```python
# myapp/models.py
from django.db import models
from citext import CITextField, CIEmailField


class MyModel(models.Model):
    name = CITextField()
    email = CIEmailField(unique=True)
```

```python
# myapp/views.py
from django.http import HttpResponse, HttpResponseNotFound

from . import models


def my_view(request, email):
    try:
        my_model = models.MyModel.objects.get(email=email)
    except models.MyModel.DoesNotExist:
        return HttpResponseNotFound()
    return HttpResponse(my_model.name)
```

## Credits

Project is based on the Django's own CITEXT implementation,
which was removed in Django 5.0. Big thanks to the Django contributors
for their excellent work.
