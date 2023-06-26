import random

# myQueue implementation
class myQueue:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return not bool(self._items)

    def enQueue(self, item):
        self._items.insert(0, item)

    def deQueue(self):
        return self._items.pop()

    def size(self):
        return len(self._items)
    
    def __init__(self):
        self._items = []

    def is_empty(self):
        return not bool(self._items)

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()

    def size(self):
        return len(self._items)

def random_100():
    return random.randint(1, 100)

def random_5():
    return random.randint(1, 5)

def fill_queue(queue, num_elements):
    for item in range(num_elements):
        queue.enQueue(random_100())

def small_q(queue1, queue2, queue3):
    if queue1.size() < queue2.size() and queue1.size() < queue3.size():
        return queue1
    elif queue2.size() < queue1.size() and queue2.size() < queue3.size():
        return queue2
    elif queue3.size() < queue1.size() and queue3.size() < queue2.size():
        return queue3
    elif queue1.size() == queue2.size():
        return queue1  
    elif queue1.size() == queue3.size():
        return queue1
    else:
        return queue2

def large_q(queue1, queue2, queue3):
    if queue1.size() > queue2.size() and queue1.size() > queue3.size():
        return queue1
    elif queue2.size() > queue1.size() and queue2.size() > queue3.size():
        return queue2
    elif queue3.size() > queue1.size() and queue3.size() > queue2.size():
        return queue3
    elif queue1.size() == queue2.size():
        return queue1
    elif queue1.size() == queue3.size():
        return queue1
    else:
        return queue2


q1 = myQueue()
q2 = myQueue()
q3 = myQueue()

fill_queue(q1, random_5())
fill_queue(q2, random_5())
fill_queue(q3, random_5())

print(q1._items)
print(q2._items)
print(q3._items)

smallQ = small_q(q1, q2, q3)
print(smallQ._items)
smallQ.enQueue(42)
print("Item added to Queue with least amount of elements.")
print(smallQ._items)
print("\n")

largeQ = large_q(q1, q2, q3)
print(largeQ._items)
largeQ.deQueue()
print("Item removed from Queue with most amount of elements.")
print(largeQ._items)