// ? 对应的图解: https://leetcode.cn/problems/swap-nodes-in-pairs/solution/shou-hua-tu-jie-24-liang-liang-jiao-huan-lian-biao/
var swapPairs = function (head) {
    //* 因为两两交换完节点后, 头节点可能会改变, 需要一个虚拟头节点方便返回

    let dummyNode = new ListNode(0);
    dummyNode.next = head;
    let prevNode = dummyNode;
    let current = head;

    //* 在这里要交换的是 current 与 nextNode, 由于 while 中 current 和 current.next 非空的判断所以 current 和 nextNode 一定都不为空。判断 current 非空: 对应了如果是「空链表」&&「链表有偶数个节点」, current 在更新后指向空, 判断 current.next 非空: 对应「链表有奇数个节点」的情况, current 在更新后指向最后一个节点; 这两个情况都不会再次进入循环导致 undefined.next 的报错。
    while (current !== null && current.next !== null) {
        let nextNode = current.next;
        //* 偷个懒, 只要记录了这个节点, 剩下的交换顺序可以随意
        let tempNode = nextNode.next;
        prevNode.next = nextNode;
        nextNode.next = current;
        current.next = tempNode;

        /// current 的经过交换前的位置就是本轮两个要交换node的前一个, 经过交换后是在下一轮要交换的 node 对整体的前一个 node, 我们在下面要更新 current, 从而让他到下一轮两个要交换的 node 上, 这里顺序很重要; prevNode 要先更新, 否则 current 更新后就失去了标记
        prevNode = current;
        current = current.next;
    }

    return dummyNode.next;
};
