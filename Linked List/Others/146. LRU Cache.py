""" 
* LRU （Least Recently Used）缓存机制
* 在缓存满的时候, 删除缓存里最久未使用的数据, 然后再放入新元素；
* 数据的访问时间很重要, 访问时间距离现在最近, 就最不容易被删除。
* 如果我们每次默认从「链表尾部」添加元素, 那么显然「越靠尾部」的元素就是「最近使用」的, 「越靠头部」的元素就是「最久未使用」的。
? python 代码: https://leetcode.cn/problems/lru-cache/solution/lru-ce-lue-xiang-jie-he-shi-xian-by-labuladong/

* 分析的过程: 
* ➊ 看到题目要我们实现一个可以存储 key-value 形式数据的数据结构，并且可以记录最近访问的 key 值。首先想到的就是用字典来存储 key-value 结构，这样对于查找操作时间复杂度就是 O(1)。
* ➋ 但是因为字典本身是无序的，所以我们还需要一个类似于「队列」的结构来记录访问的「先后顺序」这个队列需要支持如下几种操作：
    * Ⅰ. 在末尾加入一项
    * Ⅱ. 去除最前端一项
    * Ⅲ. 将队列中某一项移到末尾
    
* ➌ 首先考虑使用 python 中的 list, 加入有 append(), 删除有 pop() 操作, 这两个都是 O(1) 的时间复杂度。但是对于「将队列中某一项移到末尾」, 无法在常数时间内把它挑出来并移到队尾
* ➍ 再考虑使用 singly linked list, 遇到「将队列中某一项移到末尾」情况时可以在常数的时间内「找到对应的节点」, 但是如果想将它「移到尾部」则需要「从头遍历」到该节点才能保证链表不断, 所以对于这种情况需要的时间复杂度也是 O(n)
* ➎ 解决「移到尾部」这个问题, 需要使用『双链表』来记录, 结构大概如下图所示：
? https://leetcode.cn/problems/lru-cache/solution/shu-ju-jie-gou-fen-xi-python-ha-xi-shuang-xiang-li/
"""



class Node:
    def __init__(self, key = None, val = None):
        self.val = val
        self.key = key
        self.next = None
        self.pre = None

class DoubleList:
    def __init__(self):
        #* 定义虚拟头节点以及虚拟尾节点: head ⇆ node1 ⇆ tail. 定义的作用就是在删除和插入节点时方便操作。
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head
        self.size = 0
    
    #* 在链表尾部添加节点 newNode, 时间 O(1)
    def addLast(self, newNode):
        #* 首先将 newNode 的 pre指针, next指针进行安排
        newNode.pre = self.tail.pre
        newNode.next = self.tail
        self.tail.pre.next = newNode
        self.tail.pre = newNode
        self.size += 1
    
    #* 删除链表中的 node 节点（node 一定存在）
    #* 由于是双链表且给的是目标 node 节点, 时间 O(1)
    def remove(self, deleteNode):
        deleteNode.pre.next = deleteNode.next
        deleteNode.next.pre = deleteNode.pre
        deleteNode.next = None
        deleteNode.pre = None
        self.size -= 1

    #* 删除链表中第一个节点, 并返回该节点, 时间 O(1)
    def removeFirst(self):
        if self.getSize() == 0:
            return None
        firstNode = self.head.next
        self.remove(firstNode)
        return firstNode
    
    #* 返回链表长度, 时间 O(1)
    def getSize(self):
        return self.size

class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        
        #* map 中存储的「键值对」是 key -> node
        self.map = {}
        
        #* cache 中存储的是「doubly linked list」, 形式是 head ⇆ node1 ⇆ node2 ⇆ tail
        self.cache = DoubleList()


    def get(self, key):
        #* if the key does not exist, return -1
        if key not in self.map:
            return -1
        
        #* if the key exists, make it the recently used node
        returnedNode = self.map[key]
        #* put function 能起到将某个节点更新并放在最近被使用的位置
        self.put(key, returnedNode.val)
        return returnedNode.val


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        newNode = Node(key, value)
        #* 若 key 已经存在, 首先从 map 中获取对应的节点, 在 cache 中删除对应的节点, 并在末尾添加新节点 newNode, 代表它是最近被使用的节点
        if key in self.map:
            existNode = self.map[key]
            self.cache.remove(existNode)
            self.cache.addLast(newNode)
            self.map[key] = newNode
        else:
            #* 若 key 不存在, 又分为两种情况：
            if self.cache.getSize() == self.capacity:               
                #* 1. 容量已满, 淘汰最久未使用的node, 也就是 firstNode, 并将其从 hashmap 以及 cache 中都移除. 然后在 map 以及 cache 中插入新的节点
                firstNode = self.cache.removeFirst()
                self.map.pop(firstNode.key)
                self.cache.addLast(newNode)
                self.map[key] = newNode
            else:
                #* 2. 容量未满, 直接在 map 以及链表中插入 key 和 newNode
                self.cache.addLast(newNode)
                self.map[key] = newNode
    
        
    
    def printCache(self):
        head = self.cache.head
        result = []
        while head != None:
            result.append(head.val)
            head = head.next
        return result

