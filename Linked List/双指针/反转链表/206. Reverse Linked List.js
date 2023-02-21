/*
* 我们可以申请两个指针，第一个指针叫 pre，最初是指向 null 的。
* 第二个指针 cur 指向 head，然后不断遍历 cur。
* 每次迭代到 cur，都将 cur 的 next 指向 pre，然后 pre 和 cur 前进一位。
* 都迭代完了(cur 变成 null 了)，pre 就是最后一个节点了。
//? https://leetcode-cn.com/problems/reverse-linked-list/solution/dong-hua-yan-shi-206-fan-zhuan-lian-biao-by-user74/
 */

var reverseList = function (head) {
    let prevPointer = null;
    let currentPointer = head;
    while (currentPointer !== null) {
        // 用于记录 currentPointer 指向的下一个node, 否则我们更新 currentPointer 指向后就无法得到这个node了
        let temp = currentPointer.next;
        currentPointer.next = prevPointer;
        prevPointer = currentPointer;
        currentPointer = temp;
    }
    return prevPointer;
};
