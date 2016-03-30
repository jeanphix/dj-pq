from django.db import connections

from pq.tasks import PQ, Queue as BaseQueue


_pqs = dict()


class Queue(BaseQueue):
    def __init__(self, name, connection_name):
        super(Queue, self).__init__(name)
        self.connection_name = connection_name

    def _conn(self):
        return connections[self.connection_name].cursor().connection


def get_queue(name, connection_name='default'):
    try:
        return _pqs[connection_name][name]

    except KeyError:
        return _pqs.setdefault(connection_name, PQ(
            connection_name,
            queue_class=Queue,
        ))[name]
