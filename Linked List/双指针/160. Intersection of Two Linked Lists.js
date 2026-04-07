/* 
/ 时间复杂度：O(M + N), M, N 分别为两个链表的长度。
/ 空间复杂度：O(1)。
* 因为如果链表A和链表B相交于D的话,那么说明 D 结点即在 A 上又在 B 上,而 D 之后的元素自然也就均在 A 和 B 上了,因为他们是通过next指针相连的.

* null 这一步的核心作用就是：当两个链表不相交时，两个指针能够同时到达 null，使得 ptA === ptB（都为 null），从而正确退出循环。
* 如果跳过了 null，指针会直接从一个链表的尾节点跳到另一个链表的头节点，在不相交的情况下它们永远不会指向同一个节点，导致死循环。
* 总结一下 null 步的两个作用：
    ! - 终止条件：不相交时，两指针同时到 null，ptA === ptB 成立，返回 null（正确结果）
    * - 步数对齐：相交时，经过 null 这一步保证两个指针走的总步数严格相等: lenA+lenB+1 确保它们在交点处相遇
? https://leetcode-cn.com/problems/intersection-of-two-linked-lists-lcci/solution/dai-ma-jie-shi-shuang-zhi-zhen-suan-fa-wei-shi-yao/

*/

var getIntersectionNode = function (headA, headB) {
    let p1 = headA;
    let p2 = headB;
    // > 关键在于让 p1 p2 在每一次 while 循环结束时都走相同的步数
    //! 虽然 p1 p2 这两个指针都多走了一步，这一步就是走到null的一步，它们是先到null，然后再到另一个头节点，但因为两个指针都多走了，依旧是走了相同的步数，所以互相抵消，不影响结果
    /// 如果没有交点的话且长度不同，两个指针分别走完两个链表后会一起到 null, 这时候不满足 while 循环条件跳出循环。他们两个第一次分别走到null时，另一个指针并不在null，所以不会退出循环
    while (p1 !== p2) {
        if (p1 === null) p1 = headB;
        else p1 = p1.next;

        if (p2 === null) p2 = headA;
        else p2 = p2.next;
    }
    return p1;
};
