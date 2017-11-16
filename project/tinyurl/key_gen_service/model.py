from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model


class Key(Model):
    __keyspace__ = 'tinyurl'
    id = columns.Ascii(primary_key=True, min_length=6, max_length=6)
    available = columns.Boolean(primary_key=True, default=True)

