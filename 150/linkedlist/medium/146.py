# 0. will have a double ll as adt for constant deletion/insertion
class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
    

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.total = 0
        self.storage = {}
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        # 1. dictionary will hold value and link to node place in dll
        # 2. node will hold key,value and its position will be the key rank
    
    def remove(self, node):
        # 3. removes node by seting next and prev of before/after nodes
        before = node.prev
        after = node.next
        before.next = after
        after.prev = before
        return node.key
    
    def insert(self, node):
        # 4. inserts node to head of dll
        nexth = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = nexth
        nexth.prev = node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # 5. check if node exists and changes node location
        if key not in self.storage: return -1
        node = self.storage[key]
        self.remove(node)
        self.insert(node)
        return node.value
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """ 
        # 6. if node exists update value and insert at front
        if key in self.storage:
            node = self.storage[key]
            self.remove(node)
            self.insert(node)
            node.value = value
            return
        
        # 7. if new node increment total and check against capacity
        self.total += 1
        new_node = ListNode(key, value)
        self.storage[key] = new_node
        self.insert(new_node)
        if self.total > self.capacity:
            key = self.remove(self.tail.prev)
            del self.storage[key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)