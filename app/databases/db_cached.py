import json
import rocksdb


class DBCached:
    def __init__(self, directory='cached_data.db', read_only=False):
        self.db = rocksdb.DB(directory, rocksdb.Options(
        create_if_missing=True), read_only=read_only)

    def get_by_key_query(self, key_query, default=None):
        cached_value = self.db.get(key_query.encode())

        if cached_value is None:
            return default

        cached_value = json.loads(cached_value)
        return cached_value

    def save_cached(self, cached_data):
        for key, value_to_cache in cached_data.items():
            self.db.put(key.encode(), json.dumps(value_to_cache).encode())