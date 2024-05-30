# STACK CAN HOLD ANYTHING INCLUDING LISTS
# stack will hold element 

class MinStack(object):

    def __init__(self):
        self.min_stack = []
        self.running = None
        
    def push(self, val):
        if len(self.min_stack) == 0:
            self.running = val
        if val < self.running: self.running = val
        self.min_stack.append([val, self.running])

    def pop(self):
        v1, v2 = self.min_stack.pop()
        if self.min_stack: self.running = self.min_stack[-1][1]
        
    def top(self):
        return self.min_stack[-1][0]
        
    def getMin(self):
        return self.min_stack[-1][1]


# HEAP SOLUTION


class MinStack(object):

    def __init__(self):
        self.stack = []
        self.heap = []
        
    def push(self, val):
        self.stack.append(val)
        heapq.heappush(self.heap, val)
        
    def pop(self):
        self.stack.pop()
        
    def top(self):
        return self.stack[-1]

    def getMin(self):
        elem = heapq.heappop(self.heap)
        while elem not in self.stack:
            elem = heapq.heappop(self.heap)
        heapq.heappush(self.heap, elem)
        return elem