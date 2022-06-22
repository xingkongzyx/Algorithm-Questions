var reverseList = function (head) {
    let pre = null;
    let current = head;
    while (current !== null) {
        next = current.next;
        current.next = pre;
        pre = current;
        current = next;
    }
    return pre;
};
