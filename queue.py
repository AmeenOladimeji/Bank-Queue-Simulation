# Author: Bomi Oladimeji
# ID: 3164447
# Course: CMPT 200
# Assignment: Lab 3 
# Collaborators: Lab instructor
# Sources: Course lab materials

import numpy as np 

class Empty(Exception):
    """
    purpose: Custom exception raised when queue operations are attempted on an empty queue.
    """
    pass

class Queue:
    """
    This is an array-based dynamic circular queue class that uses numpy arrays 
    with object type elements for the underlying data structure.
    """
    def __init__(self, capacity = 5):
        """
        purpose: initialize the queue with a default or specified capacity
        parameters: capacity: integer representing the initial size of the queue
        throws: TypeError if capacity is not an integer
        pre: capacity must be a valid integer
        post: queue is initialized with a numpy array, size 0, and front at 0
        returns: none
        """
        if type(capacity) != int:
            raise TypeError('Capacity must be an integer')
        else:
            self.capacity = capacity


        self.queue = np.empty(self.capacity, dtype=object)
        self.size = 0
        self.front = 0

    def enqueue(self, value):
        """
        purpose: add a value to the rear of the queue, resizing dynamically if full
        parameters: value: the element to be added to the queue
        throws: none
        pre: queue is initialized
        post: value is added to the rear, size increases by 1, capacity doubles if full
        returns: none
        """
        if self.size == self.capacity:
            new_capacity = self.capacity * 2
            new_queue = np.empty(new_capacity, dtype=object)
            current_index = self.front 


            for i in range(self.size): 
                new_queue[i] = self.queue[current_index]
                current_index = (current_index + 1) % self.capacity

            self.front = 0
            self.capacity = new_capacity
            self.queue = new_queue
            rear_index = (self.front + self.size) % self.capacity
            self.queue[rear_index] = value
            self.size += 1
            
        else:
         rear_index = (self.front + self.size) % self.capacity
         self.queue[rear_index] = value
         self.size += 1

    def dequeue(self):
        """
        purpose: remove and return the element at the front of the queue
        parameters: none
        throws: Empty exception if the queue is empty
        pre: queue is initialized
        post: front element is removed, front pointer shifts, size decreases by 1
        returns: the value removed from the front of the queue
        """
        if self.is_empty():
            raise Empty('Cannot dequeue from an empty queue')
        return_val = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return return_val

    def peek(self):
        """
        purpose: view the element at the front of the queue without removing it
        parameters: none
        throws: Empty exception if the queue is empty
        pre: queue is initialized
        post: queue remains unchanged
        returns: the value at the front of the queue
        """
        if self.is_empty():
            raise Empty('Cannot peek from an empty queue')
        return self.queue[self.front]

    def is_empty(self):
        """
        purpose: check whether the queue contains any elements
        parameters: none
        throws: none
        pre: queue is initialized
        post: queue remains unchanged
        returns: True if the queue is empty, False otherwise
        """
        if self.size == 0:
            return True
        else:
            return False

    def __len__(self):
        """
        purpose: return the number of elements currently in the queue
        parameters: none
        throws: none
        pre: queue is initialized
        post: queue remains unchanged
        returns: integer representing the current size of the queue
        """
        return self.size

    def __repr__(self):
        """
        purpose: return an official string representation of the queue object
        parameters: none
        throws: none
        pre: queue is initialized
        post: queue remains unchanged
        returns: string showing capacity, size, and front index
        """
        return f'Queue(capacity = {self.capacity}, size = {self.size}, front = {self.front})'

    def __str__(self):
        """
        purpose: return a string representation of the underlying array
        parameters: none
        throws: none
        pre: queue is initialized
        post: queue remains unchanged
        returns: string of the numpy array elements
        """
        return f'{self.queue}' 


queue = Queue(6)

