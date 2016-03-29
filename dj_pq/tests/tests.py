from django.test import TestCase

from pq.tasks import Queue
from dj_pq import get_queue


class DjPqTest(TestCase):
    def test_get_queue(self):
        queue = get_queue('notifications')
        self.assertTrue(isinstance(queue, Queue))

    def test_get_queue_twice(self):
        queue = get_queue('notifications')
        self.assertIs(
            queue,
            get_queue('notifications'),
        )

    def test_get_queue_two_databases(self):
        queue = get_queue('notifications')
        self.assertIsNot(
            queue,
            get_queue('notifications', connection_name='another'),
        )

    def test_enqueue(self):
        queue = get_queue('notifications')

        global test_value
        test_value = 40

        @queue.task()
        def task(value):
            global test_value
            test_value += value

        task(2)

        self.assertEqual(test_value, 40)
        self.assertTrue(queue.perform(queue.get()))
        self.assertEqual(test_value, 42)

        del test_value
