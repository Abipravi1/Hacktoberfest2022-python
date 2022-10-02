# Time Complexity: O(1)
# Space Complexity: O(N)
class MyCircularQueue:

    def __init__(self, k: int):
        # the queue holding the elements for the circular queue
        self.q = [0] * k
        # the number of elements in the circular queue
        self.cnt = 0
        # queue size
        self.sz = k
        # the idx of the head element
        self.headIdx = 0
        

    def enQueue(self, value: int) -> bool:
        # handle full case
        if self.isFull(): return False
		# Given an array of size of 4, we can find the position to be inserted using the formula
		# targetIdx = (headIdx + cnt) % sz
		# e.g. [1, 2, 3, _]
		# headIdx = 0, cnt = 3, sz = 4, targetIdx = (0 + 3) % 4 = 3
		# e.g. [_, 2, 3, 4]
		# headIdx = 1, cnt = 3, sz = 4, targetIdx = (1 + 3) % 4 = 0
        self.q[(self.headIdx + self.cnt) % self.sz] = value
        # increase the number of elements by 1
        self.cnt += 1
        return True

    def deQueue(self) -> bool:
        # handle empty case
        if self.isEmpty(): return False
        # update the head index
        self.headIdx = (self.headIdx + 1) % self.sz
        # decrease the number of elements by 1
        self.cnt -= 1
        return True

    def Front(self) -> int:
        # handle empty queue case
        if self.isEmpty(): return -1
        # return the head element
        return self.q[self.headIdx]
        
    def Rear(self) -> int:
        # handle empty queue case
        if self.isEmpty(): return -1
        # Given an array of size of 4, we can find the tail using the formula
        # tailIdx = (headIdx + cnt - 1) % sz
        # e.g. [0 1 2] 3
        # headIdx = 0, cnt = 3, sz = 4, tailIdx = (0 + 3 - 1) % 4 = 2
        # e.g. 0 [1 2 3]
        # headIdx = 1, cnt = 3, sz = 4, tailIdx = (1 + 3 - 1) % 4 = 3
        # e.g. 0] 1 [2 3
        # headIdx = 2, cnt = 3, sz = 4, tailIdx = (2 + 3 - 1) % 4 = 0
        return self.q[(self.headIdx + self.cnt - 1) % self.sz]

    def isEmpty(self) -> bool:
        # no element in the queue
        return self.cnt == 0

    def isFull(self) -> bool:
        # return True if the count is equal to the queue size
        # else return False
        return self.cnt == self.sz


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
