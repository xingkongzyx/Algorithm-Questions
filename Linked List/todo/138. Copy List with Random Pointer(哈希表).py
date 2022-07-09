
""" 
* 第一步: 先不考虑 random 指针, 和原本的链表复制一样, 创建新新节点, 并构造 next 指针关系, 同时使用「哈希表」记录原节点和新节点的映射关系；
* 第二步: 对原链表和新链表进行同时遍历, 对于原链表的每个节点上的 random 都通过「哈希表」找到对应的新 random 节点, 并在新链表上构造 random 关系。
/ 时间复杂度：O(n)
/ 空间复杂度：O(n)    
"""
class Solution(object):
    def copyRandomList(self, head):
        dummyHead = Node(0)
        newListPointer = dummyHead
        oldListPointer = head
        map = {}
        #* 将「原链表」中的所有节点以及对应的「next 指针关系」进行 deep clone. 同时将在「原链表」中的 node 以及其在「新链表」中的新创建的 newNode 的映射关系在 map 中进行记录
        while oldListPointer != None:
            newNode = Node(oldListPointer.val)
            newListPointer.next = newNode
            map[oldListPointer] = newNode
            oldListPointer = oldListPointer.next
            newListPointer = newListPointer.next
        
        #* 将「原链表」中的 random 指针在「新链表」中进行 deep clone 操作
        newListPointer = dummyHead.next
        oldListPointer = head
        while oldListPointer != None:
            #* randomNodeInOldList 代表了「原链表」中「当前 node」的 random 指针指向的节点(这个节点是在「原链表」中的)
            randomNodeInOldList = oldListPointer.random
            
            #* random 指针指向的节点如果不是 None 的话在一定已经被记录在 map 中并且作为 key 存在, 而对应的 value 就是「新链表」已经创建好的 node
            if randomNodeInOldList != None:
                newListPointer.random = map[randomNodeInOldList]
            oldListPointer = oldListPointer.next
            newListPointer = newListPointer.next
        return dummyHead.next
