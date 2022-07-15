class Node:
    def __init__(self, key = None, val = None):
        self.prev = None
        self.next = None
        self.key = key
        self.val = val

class dbLinkedList:
    def __init__(self):
        self.head = Node(99, 99)
        self.tail = Node(99, 99)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def removeFirst(self):
        if self.size == 0:
            return None
        firstNode = self.head.next
        self.removeNode(firstNode)
        return firstNode

    def removeNode(self, delNode):
        prevNode = delNode.prev
        nextNode = delNode.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        delNode.prev = None
        delNode.next = None
        self.size -= 1
        return delNode

    def addLast(self, newNode):
        prevNode = self.tail.prev
        prevNode.next = newNode
        newNode.prev = prevNode
        newNode.next = self.tail
        self.tail.prev = newNode
        self.size += 1

class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.cache = dbLinkedList()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1

        # remove the node from the cache, put it in the cache again
        node = self.map[key]
        self.put(key, node.val)
        return node.val

    def put(self, key: int, value: int) -> None:
        newNode = Node(key, value)
        if key in self.map:
            delNode = self.map[key]
            self.cache.removeNode(delNode)
            del self.map[key]
            self.cache.addLast(newNode)
            self.map[key] = newNode
        else:
            if self.cache.size < self.capacity:
                self.cache.addLast(newNode)
                self.map[key] = newNode
            else:
                leastUsedNode = self.cache.removeFirst()
                del self.map[leastUsedNode.key]
                self.cache.addLast(newNode)
                self.map[key] = newNode
        
    def printCache(self):
        head = self.cache.head
        result = []
        while head != None:
            result.append(head.val)
            head = head.next
        return result


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

           



# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(1,1)
obj.put(2,2)
obj.get(1)
print("*****current: ", obj.printCache(), obj.map, "\n")
obj.put(3,3)
print("*****current: ", obj.printCache(), obj.map, "\n")
obj.get(2)
print("*****current: ", obj.printCache(), obj.map, "\n")
obj.put(4,4)
print("*****current: ", obj.printCache(), obj.map, "\n")
