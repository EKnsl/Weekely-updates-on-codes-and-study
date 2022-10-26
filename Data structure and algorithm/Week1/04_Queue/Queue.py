#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


q=Queue()


val = 4
q.enqueue(val)
print("enqueued {} in Queue".format(val))
print("Size of the Queue after adding {} : ".format(val), q.size(), end = "\n\n")

val = True
q.enqueue(val)
print("enqueued {} in Queue".format(val))
print("Size of the Queue after adding {} : ".format(val), q.size(), end = "\n\n")


val = q.dequeue()
print("Dequeued {} from Queue".format(val))
print("Size of the Queue after removing {} : ".format(val), q.size(), end = "\n\n")

val = q.dequeue()
print("Dequeued {} from Queue".format(val))
print("Size of the Queue after removing {} : ".format(val), q.size(), end = "\n\n")

#safe way to remove from Queue
try :
    val = q.dequeue()
    print("Dequeued {} from Queue".format(val))
    print("Size of the Queue after removing {} : ".format(val), q.size(), end = "\n\n")
except:
    print("Failed to dequeue because Queue is empty!")



