""" 
* LRU （Least Recently Used）缓存机制
* 在缓存满的时候，删除缓存里最久未使用的数据，然后再放入新元素；
* 数据的访问时间很重要，访问时间距离现在最近，就最不容易被删除。
* 如果我们每次默认从链表尾部添加元素，那么显然越靠尾部的元素就是最近使用的，越靠头部的元素就是最久未使用的。

? python 代码: https://leetcode.cn/problems/lru-cache/solution/tu-wen-bing-mao-xiang-jie-lruji-zhi-by-user7439t/
"""


class Node:
    def __init__(self, key = None, val = None):
        self.val = val
        self.key = key
        self.next = None
        self.pre = None

class DoubleList:
    def __init__(self):
        # 定义虚拟头节点以及虚拟尾节点。head ⇆ node1 ⇆ tail
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head
        self.size = 0
    
    #/ 在链表尾部添加节点 newNode，时间 O(1)
    def addLast(self, newNode):
        newNode.pre = self.tail.pre
        newNode.next = self.tail
        self.tail.pre.next = newNode
        self.tail.prev = newNode
        self.size += 1
    
    # 删除链表中的 node 节点（node 一定存在）
    # 由于是双链表且给的是目标 Node 节点，时间 O(1)
    def remove(self, deleteNode):
        deleteNode.pre.next = deleteNode.next
        deleteNode.next.pre = deleteNode.pre
        deleteNode.next = None
        deleteNode.pre = None
        self.size -= 1

    #* 删除链表中第一个节点，并返回该节点，时间 O(1)
    def removeFirst(self):
        if self.getSize() == 0:
            return None
        firstNode = self.head.next
        self.remove(firstNode)
        return firstNode
    
    #* 返回链表长度，时间 O(1)
    def getSize(self):
        return self.size

class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        # map 中存储的【键值对】是 key -> Node
        self.map = {}
        # cache 中存储的形式是 head ⇆ node1 ⇆ node2 ⇆ tail
        self.cache = DoubleList()


    def get(self, key):
        #* if the key does not exist, return -1
        if key not in self.map:
            return -1
        returnedNode = self.map[key]
        self.put(key, returnedNode.val)
        # 将其移到尾部，作为最近使用的元素
        self.cache.remove(returnedNode)
        self.cache.addLast(returnedNode)
        return returnedNode.val


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        newNode = Node(key, value)
        #* Update the value of the key if the key exists
        if key in self.map:
            existNode = self.map[key]
            self.cache.remove(existNode)
            self.cache.addLast(newNode)
            self.map[key] = newNode
        else:
            if self.cache.getSize() == self.capacity:
                # firstNode 就是目前为止 least used node, 需要被从 hashmap 以及 链表中都被移除
                firstNode = self.cache.removeFirst()
                self.map.pop(firstNode.key)
                self.cache.addLast(newNode)
            else:
                self.cache.addLast(newNode)
            self.map[key] = newNode


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
