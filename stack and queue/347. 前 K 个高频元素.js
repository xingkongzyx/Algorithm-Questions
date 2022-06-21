class MinHeap {
    constructor() {
        this.heap = [];
    }

    // O(log(n)) time | O(1) space
    siftDown(currentIdx, endIdx, heap) {
        let leftChildIdx = 2 * currentIdx + 1;
        while (leftChildIdx <= endIdx) {
            let rightChildIdx = 2 * currentIdx + 2;
            if (rightChildIdx > endIdx) rightChildIdx = -1;
            let minChildIdx;
            if (rightChildIdx !== -1) {
                minChildIdx =
                    heap[leftChildIdx][1] < heap[rightChildIdx][1]
                        ? leftChildIdx
                        : rightChildIdx;
            } else {
                minChildIdx = leftChildIdx;
            }
            if (heap[currentIdx][1] >= heap[minChildIdx][1]) {
                [heap[currentIdx], heap[minChildIdx]] = [
                    heap[minChildIdx],
                    heap[currentIdx],
                ];
                currentIdx = minChildIdx;
                leftChildIdx = currentIdx * 2 + 1;
            } else {
                return;
            }
        }
    }
    // O(log(n)) time | O(1) space
    siftUp(currentIdx, heap) {
        let parentIdx = Math.floor((currentIdx - 1) / 2);
        while (
            parentIdx >= 0 &&
            heap[currentIdx][1] < heap[parentIdx][1]
        ) {
            [heap[parentIdx], heap[currentIdx]] = [
                heap[currentIdx],
                heap[parentIdx],
            ];
            currentIdx = parentIdx;
            parentIdx = Math.floor((parentIdx - 1) / 2);
        }
    }

    peek() {
        return this.heap[0][1];
    }

    // O(log(n)) time | O(1) space
    // 移除 root value(smallest value in min heap)
    // 具体步骤: 将 heap中的root value 与最后一个 value 交换，然后移除最后一个 value. 最后再 siftDown 从而得到正确顺序的heap
    remove() {
        [this.heap[0], this.heap[this.heap.length - 1]] = [
            this.heap[this.heap.length - 1],
            this.heap[0],
        ];
        let removedVal = this.heap.pop();
        let endIdx = this.heap.length - 1;
        this.siftDown(0, endIdx, this.heap);
        return removedVal;
    }

    // O(log(n)) time | O(1) space
    // 向heap array加入value, 然后将这个value sift up
    insert(value) {
        this.heap.push(value);
        let currentIdx = this.heap.length - 1;
        this.siftUp(currentIdx, this.heap);
    }

    getAllElements() {
        const result = [];
        for (let [num, totalCount] of this.heap) {
            result.push(num);
        }
        return result;
    }
}

/*
 * 1. 记录每个数字出现的次数
 * 2. 把数字和对应的出现次数放到堆中（小顶堆）
 * 3. 如果堆已满（大小>=k）且当前数的次数比堆顶大，用当前元素替换堆顶元素
 * 4. 返回堆中的数字部分
 */
var topKFrequent = function (nums, k) {
    let map = {};
    for (let num of nums) {
        if (num in map) {
            map[num] += 1;
        } else {
            map[num] = 1;
        }
    }
    let heap = new MinHeap();
    let count = 0;

    // 构建min heap, 如果heap中目前已经拥有了k个elements则我们对其min value(也就是root node) 与新加入的 map[num] 进行对比。因为需要的是高频元素，所有如果times < map[num], 那么就移除 root node 并且加入新的node
    for (let num in map) {
        if (count >= k) {
            let times = heap.peek();
            if (times < map[num]) {
                heap.remove();
                heap.insert([num, map[num]]);
            }
        } else {
            heap.insert([num, map[num]]);
        }
        count++;
    }
    return heap.getAllElements();
};

const nums = [1, 1, 1, 2, 2, 3];
let k = 2;
topKFrequent(nums, k);
