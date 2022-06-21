/* 
? Implement a MinHeap class that supports:
? 
? Building a Min Heap from an input array of integers.
? Inserting integers in the heap.
? Removing the heap's minimum / root value.
? Peeking at the heap's minimum / root value.
? Sifting integers up and down the heap, which is to be used when inserting and removing values.
? Note that the heap should be represented in the form of an array.
? 
? If you're unfamiliar with Min Heaps, we recommend watching the Conceptual Overview section of this question's video explanation before starting to code.

* Sample Usage
* array = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]
* 
* All operations below are performed sequentially.
* MinHeap(array): - // instantiate a MinHeap (calls the buildHeap method and populates the heap)
* buildHeap(array): - [-5, 2, 6, 7, 8, 8, 24, 391, 24, 56, 12, 24, 48, 41]
* insert(76): - [-5, 2, 6, 7, 8, 8, 24, 391, 24, 56, 12, 24, 48, 41, 76]
* peek(): -5
* remove(): -5 [2, 7, 6, 24, 8, 8, 24, 391, 76, 56, 12, 24, 48, 41]
* peek(): 2
* remove(): 2 [6, 7, 8, 24, 8, 24, 24, 391, 76, 56, 12, 41, 48]
* peek(): 6
* insert(87): - [6, 7, 8, 24, 8, 24, 24, 391, 76, 56, 12, 41, 48, 87]

*/

class MinHeap {
    constructor(array) {
        this.heap = this.buildHeap(array);
    }

    /* 
    整体方法: call the siftDown method on every parent node in the heap
    By calling the siftDown method on every parent node, you're effectively positioning every parent node correctly in the heap, and you start at very last parent node. 
    */
    // 注意 我们也可以从root node开始对每个node采取siftUp method, 但是不 optimal
    // O(n) time | O(1) space
    buildHeap(array) {
        const firstParentIdx = Math.floor((array.length - 2) / 2);

        for (
            let currentIdx = firstParentIdx;
            currentIdx >= 0;
            currentIdx--
        ) {
            this.siftDown(currentIdx, array.length - 1, array);
        }

        return array;
    }

    ​

  // O(log(n)) time | O(1) space
    siftDown(currentIdx, endIdx, heap) {
        let leftChildIdx = 2 * currentIdx + 1;
        while (leftChildIdx <= endIdx) {
            let rightChildIdx = 2 * currentIdx + 2;
            if (rightChildIdx > endIdx) rightChildIdx = -1;
            let minChildIdx;
            if (rightChildIdx !== -1) {
                minChildIdx =
                    heap[leftChildIdx] < heap[rightChildIdx]
                        ? leftChildIdx
                        : rightChildIdx;
            } else {
                minChildIdx = leftChildIdx;
            }
            if (heap[currentIdx] > heap[minChildIdx]) {
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
        while (parentIdx >= 0 && heap[currentIdx] < heap[parentIdx]) {
            [heap[parentIdx], heap[currentIdx]] = [
                heap[currentIdx],
                heap[parentIdx],
            ];
            currentIdx = parentIdx;
            parentIdx = Math.floor((parentIdx - 1) / 2);
        }
    }

    peek() {
        return this.heap[0];
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
}

// Do not edit the line below.
exports.MinHeap = MinHeap;
