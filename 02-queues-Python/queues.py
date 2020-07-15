"""Make a Queue class using a list!
Hint: You can use any Python list method
you'd like! Try to write each one in as 
few lines as possible.
Make sure you pass the test cases too!"""

class Queue:
    list1 = []
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        list1.append(new_element)
        pass

    def peek(self):
        pass 

    def dequeue(self):
        list1.pop(0)
        pass