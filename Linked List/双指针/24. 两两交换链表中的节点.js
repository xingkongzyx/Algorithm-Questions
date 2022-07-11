//? https://leetcode.cn/problems/swap-nodes-in-pairs/solution/24-liang-liang-jiao-huan-lian-biao-zhong-2kiy/
//* 因为两两交换完节点后，头节点可能会改变，需要一个虚拟头节点方便返回
var swapPairs = function (head) {
    let dummyNode = new ListNode(0);
    dummyNode.next = head;
    let current = dummyNode;

    //! 本质上我们是要交换 firstNode 和 secondNode，必须确保他们都是存在的，否则 "secondNode.next" 会报错，所以while循环继续的条件就是 "current.next && current.next.next"
    while (current.next && current.next.next) {
        let firstNode = current.next;
        let secondNode = current.next.next;
        //* 只有这句话结束才能改变 secondNode.next 指向的值，否则失去了指向 cur->1->2->Null => cur->2->1->Null
        firstNode.next = secondNode.next;
        secondNode.next = firstNode;
        current.next = secondNode;
        /// current 的更新前位置就是在本轮两个要交换node的前一个，更新后就是在下轮两个要交换node的前一个
        current = secondNode;
    }

    return dummyNode.next;
};
