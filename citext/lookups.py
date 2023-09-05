from django.db.models import Lookup, lookups


class CompareCITextLookupMixin:
    def process_lhs(self, compiler, connection, lhs=None):
        lhs_sql, params = Lookup.process_lhs(self, compiler, connection, lhs)
        return "%s::citext" % lhs_sql, list(params)


class InsensitiveCompareCITextLookupMixin:
    def process_lhs(self, compiler, connection, lhs=None):
        lhs_sql, params = Lookup.process_lhs(self, compiler, connection, lhs)
        return "UPPER(%s)" % lhs_sql, list(params)


class IsNull(lookups.IsNull):
    def process_lhs(self, compiler, connection, lhs=None):
        lhs_sql, params = Lookup.process_lhs(self, compiler, connection, lhs)
        return "%s::text" % lhs_sql, list(params)


class Contains(CompareCITextLookupMixin, lookups.Contains):
    pass


class StartsWith(CompareCITextLookupMixin, lookups.StartsWith):
    pass


class EndsWith(CompareCITextLookupMixin, lookups.EndsWith):
    pass


class Regex(CompareCITextLookupMixin, lookups.Regex):
    pass


class IRegex(CompareCITextLookupMixin, lookups.IRegex):
    pass


class IContains(InsensitiveCompareCITextLookupMixin, lookups.IContains):
    pass


class IStartsWith(InsensitiveCompareCITextLookupMixin, lookups.IStartsWith):
    pass


class IEndsWith(InsensitiveCompareCITextLookupMixin, lookups.IEndsWith):
    pass


class IExact(InsensitiveCompareCITextLookupMixin, lookups.IExact):
    pass
