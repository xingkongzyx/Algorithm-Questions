class MinHeap {
    constructor() {
        this.data = [];
        this.size = 0;
    }

    insert(val) {
        this.data.push(val);
        this.size++;
        this.siftUp(this.size - 1);
    }

    siftUp(curIdx) {
        while (curIdx > 0) {
            let parentIdx = Math.floor((curIdx - 1) / 2);
            if (this.data[curIdx] < this.data[parentIdx]) {
                this.swap(curIdx, parentIdx);
                curIdx = parentIdx;
            } else {
                break;
            }
        }
    }

    remove() {
        this.swap(0, this.size - 1);
        let topVal = this.data.pop();
        this.size--;
        this.siftDown(0);
        return topVal;
    }

    siftDown(curIdx) {
        while (2 * curIdx + 1 < this.size) {
            let childOneIdx = 2 * curIdx + 1;
            let childTwoIdx = 2 * curIdx + 2;
            let idxToSwap = childOneIdx;

            if (
                childTwoIdx < this.size &&
                this.data[childTwoIdx] < this.data[idxToSwap]
            ) {
                idxToSwap = childTwoIdx;
            }

            if (this.data[curIdx] > this.data[idxToSwap]) {
                this.swap(curIdx, idxToSwap);
                curIdx = idxToSwap;
            } else {
                break;
            }
        }
    }

    swap(idx1, idx2) {
        let temp = this.data[idx1];
        this.data[idx1] = this.data[idx2];
        this.data[idx2] = temp;
    }
}


