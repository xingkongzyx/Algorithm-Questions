/**
 * @param {ListNode} head
 * @param {number} val
 * @return {ListNode}
 */

//? https://leetcode-cn.com/problems/remove-linked-list-elements/solution/dong-hua-yan-shi-die-dai-fa-203-yi-chu-l-vfr9/

var removeElements = function (head, val) {
    let tempHead = new ListNode(0);
    tempHead.next = head;
    let current = tempHead;
    while (current.next !== null) {
        //* 在这个if 语句里我们不能使 current = current.next. 因为我们移动完next指向后不能确定当前的next是否就是我们想要的val,所以我们需要再次检查 current.next.val === val. 只有确定不是这个value，才能够移动current指针
        if (current.next.val === val)
            current.next = current.next.next;
        else current = current.next;
    }
    return tempHead.next;
};
