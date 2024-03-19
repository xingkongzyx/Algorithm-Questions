/* 
/ 通过 while (fast && fast.next) 遍历后slow 节点 - 在节点个数为偶数时 slow 的结果是中间的第二个节点；在节点个数为奇数时 slow 的结果是中间节点。
/ 所以需要一个 slow 前面的前置节点用于后续的删除操作. 

? https://leetcode.cn/problems/delete-the-middle-node-of-a-linked-list/submissions/514140673/
*/

var deleteMiddle = function (head) {
    // 当链表中只有一个节点时，我们会删除这个节点并返回空链表。但这个节点不存在前一个节点，即 pre 是没有意义的，因此对于这种情况，我们可以在遍历前进行特殊判断，直接返回空指针作为答案。
    if (head.next === null) return null;

    let slow = head;
    let fast = head;
    let pre = null;

    while (fast && fast.next) {
        pre = slow;
        slow = slow.next;
        fast = fast.next.next;
    }

    pre.next = slow.next;
    return head;
};
