/* 
将链表数据保存下来，然后依次比较每一对孪生节点和。

时间复杂度O(n), 空间复杂度O(n)
*/
var pairSum = function (head) {
    let arr = [];

    while (head) {
        arr.push(head.val);
        head = head.next;
    }

    let maxSum = -Infinity;
    let length = arr.length;
    for (let i = 0; i <= length / 2 - 1; i++) {
        let curSum = arr[i] + arr[length - 1 - i];
        maxSum = Math.max(curSum, maxSum);
    }
    return maxSum;
};
