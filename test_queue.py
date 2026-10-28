# Author: Bomi Oladimeji
# ID: 3164447
# Course: CMPT 200
# Assignment: Lab 3 
# Collaborators: None
# Sources: Course lab materials

import unittest
from queue import *

class TestQueue(unittest.TestCase):
    """
    This is a unit test class used to test all methods and exception 
    handling of the Queue class.
    """
    
    def test_queue_init(self):
        """
        purpose: test the proper initialization and default attributes of the Queue class
        parameters: none
        throws: none
        pre: Queue class is available
        post: queue object is created and attributes verified
        returns: none
        """
        queue = Queue()
        self.assertTrue(isinstance(queue, Queue))
        self.assertTrue(isinstance(queue.capacity,int))
        self.assertEqual(queue.capacity, 5)
        self.assertTrue(queue.front == 0)
        self.assertEqual(queue.size, 0)


    def test_queue_enqeue(self):
        """
        purpose: test adding items to the queue and dynamic resizing behaviour
        parameters: none
        throws: none
        pre: Queue class is available
        post: items are correctly placed in the queue and size/capacity update
        returns: none
        """
        queue = Queue()
        self.assertEqual(queue.capacity, 5 )

        queue.enqueue(1)
        self.assertEqual(queue.queue[0], 1)

        queue.enqueue(2)
        self.assertEqual(queue.queue[1], 2)

        queue.enqueue(3)
        self.assertEqual(queue.queue[2], 3)

        queue.enqueue(4)
        self.assertEqual(queue.queue[3], 4)

        queue.enqueue(5)
        self.assertEqual(queue.queue[4], 5)

        queue.enqueue(6)
       

        self.assertEqual(queue.size,6)

       

    def test_queue_deqeue(self):
        """
        purpose: test removing items from the queue and Empty exception handling
        parameters: none
        throws: Empty exception when dequeueing an empty queue
        pre: Queue class is available
        post: items are removed in FIFO order and size decreases
        returns: none
        """
        queue = Queue()
        self.assertEqual(queue.size, 0)
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)
        queue.enqueue(5)


        self.assertEqual(queue.dequeue(), 1)

        self.assertEqual(queue.dequeue(), 2)

        self.assertEqual(queue.dequeue(), 3)

        self.assertEqual(queue.dequeue(), 4)

        self.assertEqual(queue.dequeue(), 5)

        with self.assertRaises(Empty):
            queue.dequeue()

    def test_queue_peek(self):
        """
        purpose: test viewing the front element without removing it and Empty exception on empty peek
        parameters: none
        throws: Empty exception when peeking an empty queue
        pre: Queue class is available
        post: front element is correctly returned without altering queue size except via explicit dequeue
        returns: none
        """
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.peek(), 1)
        self.assertEqual(queue.size, 3)


        queue.dequeue()
        self.assertEqual(queue.peek(), 2)
        self.assertEqual(queue.size, 2)

        queue.dequeue()
        self.assertEqual(queue.peek(), 3)
        self.assertEqual(queue.size, 1)

        queue.dequeue()
        self.assertEqual(queue.size, 0)


        with self.assertRaises(Empty):
                queue.peek()

    def test_queue_is_empty(self):
        """
        purpose: test the is_empty method across various queue states
        parameters: none
        throws: none
        pre: Queue class is available
        post: returns True when empty and False when containing items
        returns: none
        """
        queue = Queue()
        self.assertTrue(queue.is_empty())

        queue.enqueue(1)
        self.assertFalse(queue.is_empty())

        queue.dequeue()
        self.assertTrue(queue.is_empty())

    def test_queue_len(self):
        """
        purpose: test the built-in len function implementation on the queue
        parameters: none
        throws: none
        pre: Queue class is available
        post: returns correct number of elements currently stored
        returns: none
        """
        queue = Queue()
        self.assertTrue(len(queue) == 0)

        queue.enqueue(1)
        self.assertTrue(len(queue) == 1)

        queue.dequeue()
        self.assertTrue(len(queue) == 0)

    def test_queue_repr(self):
        """
        purpose: test the string representation method for correctness during changes
        parameters: none
        throws: none
        pre: Queue class is available
        post: returns string matching current capacity, size, and front values
        returns: none
        """
        queue = Queue()
        self.assertEqual(repr(queue), 'Queue(capacity = 5, size = 0, front = 0)')

        queue.enqueue(1)
        self.assertEqual(repr(queue), 'Queue(capacity = 5, size = 1, front = 0)') 
        queue.enqueue('python is cool')
        self.assertEqual(repr(queue), 'Queue(capacity = 5, size = 2, front = 0)') 
        queue.enqueue(3)
        self.assertEqual(repr(queue), 'Queue(capacity = 5, size = 3, front = 0)') 
        queue.enqueue(4)
        self.assertEqual(repr(queue), 'Queue(capacity = 5, size = 4, front = 0)') 
        queue.enqueue(5)
        self.assertEqual(repr(queue), 'Queue(capacity = 5, size = 5, front = 0)') 
        queue.dequeue()
        self.assertEqual(repr(queue), 'Queue(capacity = 5, size = 4, front = 1)') 

        
 
        

if __name__ == '__main__':
    unittest.main()