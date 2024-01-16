var sortList = function (head) {
    if (head === null) return head;
    return mergeSort(head);
};

function mergeSort(head) {
    // 如果经过拆分后当前要拆分的链表只有一个节点，则不需要继续拆分 && 排序，直接返回
    if (head.next === null) return head;
    let slow = head;
    let fast = head;

    while (fast.next && fast.next.next) {
        slow = slow.next;
        fast = fast.next.next;
    }

    let head1 = head;
    let head2 = slow.next;
    slow.next = null;

    let sortedList1 = mergeSort(head1);
    let sortedList2 = mergeSort(head2);

    let dummy = new ListNode(-1);
    let cur = dummy;
    while (sortedList1 || sortedList2) {
        if (sortedList1 === null) {
            cur.next = sortedList2;
            sortedList2 = sortedList2.next;
        } else if (sortedList2 === null) {
            cur.next = sortedList1;
            sortedList1 = sortedList1.next;
        } else if (sortedList1.val < sortedList2.val) {
            cur.next = sortedList1;
            sortedList1 = sortedList1.next;
        } else {
            cur.next = sortedList2;
            sortedList2 = sortedList2.next;
        }
        cur = cur.next;
    }

    return dummy.next;
}
