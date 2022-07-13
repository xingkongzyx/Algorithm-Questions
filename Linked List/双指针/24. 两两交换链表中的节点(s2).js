// ? 对应的图解: https://leetcode.cn/problems/swap-nodes-in-pairs/solution/shou-hua-tu-jie-24-liang-liang-jiao-huan-lian-biao/
var swapPairs = function (head) {
    let dummyNode = new ListNode(0);
    dummyNode.next = head;
    let prevNode = dummyNode;
    let current = head;

    //* 在这里要交换的是 current 与 nextNode, 由于 while 中 current.next 的判断所以 nextNode 一定不为空。对应了如果是「空链表」或者「链表有奇数个节点」不会进入循环。
    while (current !== null && current.next !== null) {
        let nextNode = current.next;
        //* 偷个懒, 只要记录了这个节点，剩下的交换顺序可以随意
        let tempNode = nextNode.next;
        prevNode.next = nextNode;
        nextNode.next = current;
        current.next = tempNode;

        prevNode = current;
        current = current.next;
    }

    return dummyNode.next;
};
