/*
* 单调性关系: 每个小孩能拿到糖果个数越多，那么从当前的 piles 中能分出的 sub plies 数量就越少

题目说每个小孩必须分到相同数量的糖果且最多只能拿一堆。糖果总数已知，设为sum。假设每个小孩最多都能拿到c个糖果，那么就得分sum/c堆，这个堆数必须要大于等于小孩数量k，这样每个小孩才都能分到。那么问题就从每个小孩分的糖果数量转换成了堆数和k这个关系上。根据大小关系来调整l和r指针，来找到堆数>=k的最大c。

这个连接之处就是计算堆数的时候，由于糖果可以再细分成更小的堆数但不能合并，所以这个堆数要计算，并非简单的sum/c就够了。假设每个小孩能分到糖果mid，那么遍历candies里的candy时，堆数+=candy/mid，这样得到的堆数才是物尽其用的堆数，用这个堆数和k进行比较，从而调整r和l指针


? https://leetcode.cn/problems/maximum-candies-allocated-to-k-children/solutions/1392808/by-algo-goer-h71i/

 */
var maximumCandies = function (candies, k) {
    let sum = 0;

    for (let candy of candies) {
        sum += candy;
    }

    let left = 0;
    let right = Math.floor(sum / k);

    while (left < right) {
        // 每个孩子可以得到的糖果的数量
        let mid = Math.floor((left + right + 1) / 2);

        let heaps = 0;

        // 根据"每个孩子可以得到的糖果的数量"，当前每堆糖果如何拆分成更小的子堆，并将所有子堆的个数进行累加
        for (let candy of candies) {
            let subpiles = Math.floor(candy / mid);
            heaps += subpiles;
        }

        // 按照当前糖果分法最终可以分得的堆数比孩子的数量 k 少，说明每个孩子被分得的糖果数量应该减少，才能获得更多的堆数
        if (heaps < k) {
            right = mid - 1;
        } else {
            // 因为求的是最大值，即使相等，也要继续尝试每个孩子获得更多的糖果个数
            left = mid;
        }
    }

    return left;
};
