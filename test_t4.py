import unittest
from t4 import List, Stack, Queue


class TestList(unittest.TestCase):

    def setUp(self):
        self.list1 = List([1, 2])
        self.list2 = List()

    def test_init(self):
        self.assertIsNotNone(List())
        self.assertIsNotNone(List([1, 2, 3]))
        self.assertRaises(TypeError, List, '123')

    def test_insert(self):
        self.assertIsNone(self.list1.insert(2, 3))
        self.assertIsNone(self.list1.insert(3, 4))
        self.assertRaises(IndexError, self.list1.insert, 10, 10)
        self.assertRaises(IndexError, self.list2.insert, 1, 10)

    def test_get(self):
        self.assertIsNotNone(self.list1.get(0))
        self.assertRaises(IndexError, self.list2.get, 0)

    def test_delete(self):
        self.assertIsNone(self.list1.delete(1))
        self.assertRaises(IndexError, self.list2.delete, 0)

    def test_find(self):
        self.assertIsNotNone(self.list1.find(2))
        self.assertIsNone(self.list1.find(3))

    def test_return(self):
        self.assertEqual(self.list1.return_list(), [1, 2])
        self.assertEqual(self.list2.return_list(), [])

    def test_size(self):
        self.assertEqual(self.list1.size(), 2)
        self.assertEqual(self.list2.size(), 0)

    def tearDown(self):
        pass


class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_init(self):
        self.assertIsNotNone(Stack())
        self.assertRaises(TypeError, Stack, 1)

    def test_push(self):
        self.assertIsNone(self.stack.push(3))
        self.assertIsNone(self.stack.push(5))

    def test_pull(self):
        self.assertIsNone(self.stack.pull())

    def test_return(self):
        self.assertEqual(self.stack.return_stack(), [])

    def test_size(self):
        self.assertEqual(self.stack.size(), 0)

    def tearDown(self):
        pass


class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()

    def test_init(self):
        self.assertIsNotNone(Queue())
        self.assertRaises(TypeError, Queue, 1)

    def test_push(self):
        self.assertIsNone(self.queue.push(3))
        self.assertIsNone(self.queue.push(5))

    def test_pull(self):
        self.assertIsNone(self.queue.pull())

    def test_return(self):
        self.assertEqual(self.queue.return_queue(), [])

    def test_size(self):
        self.assertEqual(self.queue.size(), 0)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
