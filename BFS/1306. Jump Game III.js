// # 每个点只需要访问一次，因为如果该点不能跳到0，那么通过其他跳法跳到该点也不能跳到0，所以每访问一个点我们就需要记录一次。也就是代码中的visited[idx] = True

var canReach = function (arr, start) {
    if (arr[start] === 0) return true;
    const queue = [start];
    const visited = new Array(arr.length).fill(false);
    visited[start] = true;

    while (queue.length) {
        let curNode = queue.shift();

        let left = curNode - arr[curNode];
        let right = curNode + arr[curNode];

        if (left >= 0 && visited[left] === false) {
            if (arr[left] === 0) return true;
            queue.push(left);
            visited[left] = true;
        }
        if (right < arr.length && visited[right] === false) {
            if (arr[right] === 0) return true;
            queue.push(right);
            visited[right] = true;
        }
    }

    return false;
};
