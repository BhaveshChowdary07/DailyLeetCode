class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.length = k
        self.queue = []

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if len(self.queue)<self.length:
            self.queue.append(value)
            return True
        return False

    def deQueue(self):
        """
        :rtype: bool
        """
        if len(self.queue)>0:
            self.queue.reverse()
            self.queue.pop()
            self.queue.reverse()
            return True
        return False

    def Front(self):
        """
        :rtype: int
        """
        return self.queue[0] if len(self.queue)>0 else -1

    def Rear(self):
        """
        :rtype: int
        """
        return self.queue[-1] if len(self.queue)>0 else -1

    def isEmpty(self):
        """
        :rtype: bool
        """
        return False if len(self.queue) > 0 else True

    def isFull(self):
        """
        :rtype: bool
        """
        return True if len(self.queue) == self.length else False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()