import pytest

from tests.testapp import models


def test_generators():
    baker = pytest.importorskip("model_bakery.baker")
    assert baker.prepare(models.TestModel)
