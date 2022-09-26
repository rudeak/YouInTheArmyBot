from app import es
from app.build_indexes import es_index_sync

es_index_sync(es)