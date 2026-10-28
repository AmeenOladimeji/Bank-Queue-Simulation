# Bank Queue Simulation

A Python implementation of a dynamic circular queue built with NumPy, complete with a full unit test suite and a bank teller simulation system.

## Overview

This project implements a circular queue data structure from scratch. It handles automatic array resizing when full, supports efficient FIFO operations, and includes custom exception handling. It also features a bank teller simulation module to model customer wait times and service handling.

## Files Included

- **queue.py**: The core data structure class implementing a dynamic circular queue with NumPy arrays, supporting enqueue, dequeue, peek, dynamic resizing, and custom Empty exceptions.
- **test_queue.py**: A complete testing suite built using Python's unittest framework to verify queue operations, edge cases, and exception handling.
- **banking.py**: A simulation module featuring a Teller class that tracks customer service cycles, wait times, and teller availability.

## Key Features

- **Dynamic Resizing:** Automatically doubles capacity and reorganizes pointers when the queue reaches its limit.
- **Robust Error Handling:** Custom Empty exceptions to safely manage invalid operations on empty queues.
- **Comprehensive Testing:** Validates initialization, length tracking, string representations, and FIFO ordering.
- **Clean Documentation:** Fully commented with clear purpose statements, parameters, and method behaviors across all files.

## Quick Example

```python
from queue import Queue

# Initialize a queue
q = Queue(capacity=3)

# Add items
q.enqueue("Alice")
q.enqueue("Bob")

# Check front and remove
print(q.peek())  # Alice
print(q.dequeue())  # Alice
