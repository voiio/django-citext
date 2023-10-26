import pytest
from model_bakery import baker

from tests.testapp import models


@pytest.mark.django_db
def test_generators():
    assert baker.prepare(models.TestModel)
