/* 
/ 时间复杂度：O(M + N), M, N 分别为两个链表的长度。
/ 空间复杂度：O(1)。
* 因为如果链表A和链表B相交于D的话,那么说明D结点即在A上又在B上,而D之后的元素自然也就均在A和B上* 了,因为他们是通过next指针相连的.

* 如果有相交的结点D的话,每条链的头结点先走完自己的链表长度,然后回头走另外的一条链表,那么两结点一定为相交于D点,因为这时每个头结点走的距离是一样的,都是 AD + BD + DC,而他们每次又都是前进1,所以距离相同,速度又相同,固然一定会在相同的时间走到相同的结点上,即D点

* 1 如果不相交且两个链表长度不相等 一个为A 一个为B ，指针第一次走完A会去走B,另一个走完B再去走 A，两个指针走的路程都是 A + B。会同时为NULL 跳出循环
* 2 如果不相交且链表长度相等: 那么一个指针走A,一个指针走B，它俩同时走到NULL，相等，跳出循环

? https://leetcode-cn.com/problems/intersection-of-two-linked-lists-lcci/solution/dai-ma-jie-shi-shuang-zhi-zhen-suan-fa-wei-shi-yao/

*/

var getIntersectionNode = function (headA, headB) {
    let p1 = headA;
    let p2 = headB;
    //! 相当于 p1 p2 这两个指针都多走了一步，这一步就是走到null的一步，它们是先到null，然后再到另一个头节点，但因为两个指针都多走了，所以互相抵消，不影响结果
    /// 如果没有交点的话且长度不同，两个指针分别走完两个链表后会一起到 null, 这时候不满足 while 循环条件跳出循环。他们两个第一次分别走到null时，另一个指针并不在null，所以不会退出循环
    while (p1 !== p2) {
        if (p1 === null) p1 = headB;
        else p1 = p1.next;

        if (p2 === null) p2 = headA;
        else p2 = p2.next;
    }
    return p1;
};
