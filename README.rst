dj-pq
=====

`pq <https://github.com/malthe/pq>`_ wrapper for django.

.. image:: https://travis-ci.org/jeanphix/dj-pq.svg?branch=master
    :target: https://travis-ci.org/jeanphix/dj-pq


Installation
------------


.. code-block:: bash

    pip install dj-pq


Configuration
-------------

Add ``dj_pq`` to your ``INSTALLED_APPS``:

.. code-block:: python

    INSTALLED_APPS += [
        'dj_pq',
    ]


Apply migrations::

    ./manage.py migrate


Usage
-----

``dj-pq`` exposes the `pq tasks API <https://github.com/malthe/pq/#tasks>`_.

.. code-block:: python

    from dj_pq import get_queue

    queue = get_queue('notifications')

    @queue.task()
    def notify(user_id):
        User.objects.get(id=user_id).notify()

    notify(42)


Optionally a ``Queue`` can be bound to a specific database connection:

.. code-block:: python

    queue = get_queue('notifications', 'another_connection')


A ``worker`` command allows to start a worker for a given queue::

    ./manage.py worker notifications
