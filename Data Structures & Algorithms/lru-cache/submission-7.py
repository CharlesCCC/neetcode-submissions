class Node:
    def __init__(self, key, val) -> None:
        self.key, self.val = key, val 
        self.prev = self.next = None 

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        # Two Dummy nodes to hold for Left(Least Recent) and right(Most Recent)
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next = self.right 
        self.right.prev = self.left 

    def remove(self,node):
        prev, nxt = node.prev, node.next 
        prev.next = nxt 
        nxt.prev = prev

    def insert(self,node):
        prev = self.right.prev
        nxt = self.right
        prev.next = nxt.prev = node 
        node.next = nxt 
        node.prev = prev 

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val 
        return -1 

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next 
            self.remove(lru)
            del self.cache[lru.key]
        
