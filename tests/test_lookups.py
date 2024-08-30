import pytest

from tests.testapp import models


@pytest.mark.django_db
class TestIsNull:
    def test_cast(self):
        models.TestModel.objects.create(text="SearchTerm")
        qs = models.TestModel.objects.filter(text__isnull=False)
        assert qs.exists()
        assert 'WHERE "testapp_testmodel"."text"::text IS NOT NULL' in str(qs.query)


class CITextLookupTestMixin:
    lookup = ""
    lhs = ""
    rhs = ""
    operator = ""
    term = "searchterm"

    def test_cast(self):
        models.TestModel.objects.create(text="SearchTerm")
        qs = models.TestModel.objects.filter(**{f"text__{self.lookup}": self.term})
        assert qs.exists()
        assert f"WHERE {self.lhs} {self.operator} {self.rhs}" in str(qs.query)


@pytest.mark.django_db
class TestContains(CITextLookupTestMixin):
    lookup = "contains"
    lhs = '"testapp_testmodel"."text"::citext'
    rhs = "%cht%"
    operator = "LIKE"
    term = "cht"


@pytest.mark.django_db
class TestStartsWith(CITextLookupTestMixin):
    lookup = "startswith"
    lhs = '"testapp_testmodel"."text"::citext'
    rhs = "search%"
    operator = "LIKE"
    term = "search"


@pytest.mark.django_db
class TestEndsWith(CITextLookupTestMixin):
    lookup = "endswith"
    lhs = '"testapp_testmodel"."text"::citext'
    rhs = "%term"
    operator = "LIKE"
    term = "term"


@pytest.mark.django_db
class TestRegex(CITextLookupTestMixin):
    lookup = "regex"
    lhs = '"testapp_testmodel"."text"::citext'
    rhs = ".*term"
    operator = "~"
    term = ".*term"


@pytest.mark.django_db
class TestIRegex(CITextLookupTestMixin):
    lookup = "iregex"
    lhs = '"testapp_testmodel"."text"::citext'
    rhs = "search.*"
    operator = "~*"
    term = "search.*"


@pytest.mark.django_db
class TestIContains(CITextLookupTestMixin):
    lookup = "icontains"
    lhs = 'UPPER("testapp_testmodel"."text")'
    rhs = "UPPER(%cht%)"
    operator = "LIKE"
    term = "cht"


@pytest.mark.django_db
class TestIStartsWith(CITextLookupTestMixin):
    lookup = "istartswith"
    lhs = 'UPPER("testapp_testmodel"."text")'
    rhs = "UPPER(search%)"
    operator = "LIKE"
    term = "search"


@pytest.mark.django_db
class TestIEndsWith(CITextLookupTestMixin):
    lookup = "iendswith"
    lhs = 'UPPER("testapp_testmodel"."text")'
    rhs = "UPPER(%term)"
    operator = "LIKE"
    term = "term"


@pytest.mark.django_db
class TestIExact(CITextLookupTestMixin):
    lookup = "iexact"
    lhs = 'UPPER("testapp_testmodel"."text")'
    rhs = "UPPER(searchterm)"
    operator = "="
    term = "searchterm"
