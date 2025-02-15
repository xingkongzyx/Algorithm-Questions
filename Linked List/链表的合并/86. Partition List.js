/* 
? https://leetcode.cn/problems/partition-list/solutions/2362068/86-fen-ge-lian-biao-shuang-zhi-zhen-qing-hha7/
! "largeOrEqIter.next = null" 没有这一句会成环。
* 假设链表是4->1->2->3，然后x是4，第一次判断head.val和x关系后，big指向值为4的节点, 而值为4的结点指向值为1的结点(注意这一点)。
* 如果你不改变big.next的指向的话，它就一直指向值为1的结点，最后small_dummy为1->2->3，big_dummy为4->1->2->3，进行连接就成了环。
* 在最终连接两个链表的时候，你把sml的尾部节点, 连入big的开头节点, 但是big的尾部节点在原链表里可能不是指向None, 从而形成环，所以这一部就是断开原链表的连接。
*/
var partition = function (head, x) {
    let smallHead = new ListNode(-1);
    let largeOrEqHead = new ListNode(-1);
    let smallIter = smallHead;
    let largeOrEqIter = largeOrEqHead;

    while (head !== null) {
        if (head.val < x) {
            smallIter.next = head;
            smallIter = smallIter.next;
        } else {
            largeOrEqIter.next = head;
            largeOrEqIter = largeOrEqIter.next;
        }
        head = head.next;
    }
    // console.log(smallHead)
    // console.log(largeOrEqHead)
    smallIter.next = largeOrEqHead.next;
    largeOrEqIter.next = null;
    return smallHead.next;
};
