class MinHeap {
    constructor(array) {
        this.heap = this.buildHeap(array);
    }

    //call siftdown method on every parent node on the tree
    buildHeap(array) {
        let firstParentIdx = Math.floor((array.length - 2) / 2);
        for (
            let currentIdx = firstParentIdx;
            currentIdx >= 0;
            currentIdx--
        ) {
            this.siftDown(currentIdx, array.length - 1, array);
        }
        return array;
    }

    //compare it with its two children nodes's smaller value
    // if it is larger than currentNode, then swap it
    siftDown(currentIdx, endIdx, heap) {
        let childOne = 2 * currentIdx + 1;
        // 确保至少有一个child index在范围内
        while (childOne <= endIdx) {
            let smallerIdx;
            let childTwo = 2 * currentIdx + 2;
            // child two index out of range
            if (childTwo > endIdx) smallerIdx = childOne;
            else {
                // child two is inside the range, get the smaller index with
                // smaller value
                if (heap[childOne] > heap[childTwo])
                    smallerIdx = childTwo;
                else smallerIdx = childOne;
            }
            // campare it with currrent value
            if (heap[smallerIdx] < heap[currentIdx]) {
                let tempVal = heap[smallerIdx];
                heap[smallerIdx] = heap[currentIdx];
                heap[currentIdx] = tempVal;

                currentIdx = smallerIdx;
                childOne = 2 * currentIdx + 1;
            } else {
                break;
            }
        }
    }

    siftUp(currentIdx, heap) {
        let childIdx = currentIdx;
        let parentIdx = Math.floor((childIdx - 1) / 2);
        //while our current node is smaller than its parent node,
        //swap it
        while (currentIdx > 0 && heap[parentIdx] > heap[childIdx]) {
            let temp = heap[parentIdx];
            heap[parentIdx] = heap[childIdx];
            heap[childIdx] = temp;

            childIdx = parentIdx;
            parentIdx = Math.floor((childIdx - 1) / 2);
        }
    }

    peek() {
        // Write your code here.
        return this.heap[0];
    }

    remove() {
        //swap root value with the last value in heap
        let temp = this.heap[0];
        this.heap[0] = this.heap[this.heap.length - 1];
        this.heap[this.heap.length - 1] = temp;
        let removedVal = this.heap.pop();
        // sift down
        this.siftDown(0, this.heap.length - 1, this.heap);
        return removedVal;
    }

    insert(value) {
        // push the value in to heap array
        this.heap.push(value);
        // sift up
        this.siftUp(this.heap.length - 1, this.heap);
    }

    size() {
        return this.heap.length;
    }
}
// !题目与解释 https://mp.weixin.qq.com/s/aOvqVxVlMwvPkPwgPrx0sA
// ! https://blog.csdn.net/fuxuemingzhu/article/details/100935607
/*
 * 先按照会议的开始时间升序排序一下数组
 * 我们可以维护一个最小堆用于记录结束时间，这样可以保证整个解的时间复杂度是 O(nlogn) 的。
 * 我们先查看优先队列(minHeap)中其他会议的结束时间是否小于等于当前会议的开始时间，将相比于当前会议开始时间点已经结束的会议从优先队列(minHeap)中删除，然后再将当前会议的结束时间加入到优先队列(minHeap)中。
 * 此时优先队列(minHeap)中保存的会议应该是在同时进行且还没有结束的所有会议，因此优先队列的元素个数即是我们在此刻需要的最少会议室个数，用该个数更新全局结果的最大值。直到循环结束，返回全局最大值即可。
 */

module.exports = {
    //param A : array of array of integers
    //return an integer
    solve: function (A) {
        if (A.length === 0) return 0;

        A.sort((intervalA, intervalB) => {
            if (intervalA[0] > intervalB[0]) return 1;
            else if (intervalB[0] > intervalA[0]) return -1;
            else return intervalA[1] - intervalB[1];
        });

        let minHeap = new MinHeap([]);
        let rooms = 1;
        for (let i = 0; i < A.length; i++) {
            if (minHeap.size() > 0 && minHeap.peek() <= A[i][0]) {
                minHeap.remove();
            }

            minHeap.insert(A[i][1]);

            rooms = Math.max(rooms, minHeap.size());
        }
        //> 由于优先占用释放的会议室，所以最后堆里面的元素个数表示总的需要占用多少个会议室。
        return minHeap.size();
    },
};
