/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */

//? https://leetcode.cn/problems/remove-nth-node-from-end-of-list/solution/dong-hua-yan-shi-kuai-man-zhi-zhen-19-sh-n9ih/

var removeNthFromEnd = function (head, n) {
    let tempHead = new ListNode(0);
    tempHead.next = head;
    let slow = tempHead,
        fast = tempHead;

    //! 注意 fast 提前移动 n + 1 步(解释见上面链接的动画演示)
    while (n + 1 > 0) {
        fast = fast.next;
        n--;
    }
    //* 最后 fast 指向null时，slow指向被删除元素的前一个
    while (fast !== null) {
        slow = slow.next;
        fast = fast.next;
    }

    slow.next = slow.next.next;
    return tempHead.next;
};
