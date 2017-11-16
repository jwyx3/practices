from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model


class Url(Model):
    __keyspace__ = 'tinyurl'
    id = columns.Ascii(primary_key=True, min_length=6, max_length=6)
    url = columns.Text(primary_key=True)
    created_at = columns.DateTime()
    expired_at = columns.DateTime(required=False)

