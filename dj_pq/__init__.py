from django.db import connections

from pq.tasks import PQ, Queue


_pqs = dict()


def get_queue(name, connection_name='default'):
    try:
        return _pqs[connection_name][name]

    except KeyError:
        return _pqs.setdefault(connection_name, PQ(
            connections[connection_name].cursor().connection,
            queue_class=Queue,
        ))[name]
