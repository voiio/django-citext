from model_bakery import baker

from tests.testapp import models


def test_generators():
    assert baker.prepare(models.TestModel)
