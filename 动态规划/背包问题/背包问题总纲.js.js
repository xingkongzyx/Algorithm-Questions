//? https://leetcode-cn.com/problems/last-stone-weight-ii/solution/yi-pian-wen-zhang-chi-tou-bei-bao-wen-ti-5lfv/

//* dp[i][j] 表示从下标为[0-i]的物品里任意取，放进容量为j的背包，价值总和最大是多少。
var two_dimension_bag_problem = function (
    weights,
    values,
    bagWeight
) {
    let dp = new Array(weights.length);
    for (let i = 0; i < dp.length; i++) {
        dp[i] = new Array(bagWeight + 1).fill(0);
    }

    // 初始化:第一列都是0，第一行表示只选取0号物品最大价值
    for (let rowIdx = 0; rowIdx < weights.length; rowIdx++) {
        dp[rowIdx][0] = 0;
    }

    for (let colIdx = 0; colIdx < dp[0].length; colIdx++) {
        if (colIdx >= weights[0]) dp[0][colIdx] = values[0];
    }

    for (let itemIdx = 1; itemIdx < weights.length; itemIdx++) {
        for (let capacity = 1; capacity <= bagWeight; capacity++) {
            let itemWeight = weights[itemIdx];
            // * 如果当前位置的capacity不足够放置当前的itemIdx的物品，那么我们就要看当前位置的capacity对于上一个物品放置时的最大价值，也就是这个cell的上一行的格子。意味着从下标为[0, itemIdx-1]的物品里任意取，放进容量为capacity的背包，价值总和最大是多少。
            if (itemWeight > capacity)
                dp[itemIdx][capacity] = dp[itemIdx - 1][capacity];
            else {
                //# 如果当前位置的capacity能放置当前的itemIdx的物品，那么有两种可能一种是放置这个物品，一种是不放这个物品。不放的的话当前的最大价值是 dp[itemIdx - 1][capacity]。
                //# 如果放置的话也不是直接 dp[itemIdx - 1][capacity] + values[itemIdx]. 这么计算是不对的，dp[itemIdx - 1][capacity]是计算的从下标为[0-itemIdx-1]的物品里任意取，放进容量为capacity的地方，价值总和最大是多少。而我们在同一个capacity直接加上当前itemIdx的价值，相当于把对应的weights加到了capacity里，这样会导致当前的容量无法放置这么多东西。
                //! 而应该是 dp[itemIdx - 1][capacity - itemWeight] + values[itemIdx]。dp[itemIdx - 1][capacity - itemWeight]为背包容量为capacity - itemWeight的时候不放物品itemIdx的最大价值。那加上values[itemIdx]就是背包放物品itemIdx得到的最大价值
                dp[itemIdx][capacity] = Math.max(
                    dp[itemIdx - 1][capacity],
                    dp[itemIdx - 1][capacity - itemWeight] +
                        values[itemIdx]
                );
            }
        }
    }
    console.log(dp);
    return dp[weights.length - 1][bagWeight];
};

/* 
> 在一维dp数组中，dp[j]表示：容量为j的背包，所背的物品价值可以最大为dp[j]。

* 如何推导dp[j]呢？dp[j]可以通过dp[j - weight[i]]推导出来，dp[j - weight[i]]表示容量为j - weight[i]的背包所背的最大价值。

* dp[j - weight[i]] + value[i] 表示 容量为 (j - 物品i重量) 的背包 加上 物品i的价值。（也就是容量为j的背包，放入物品i了之后的价值即：dp[j]）

! 为什么要从后向前遍历?
/ 状态压缩会导致现在处理的物品和上一件物品用的是一个数组，对于一般背包问题必须由后向前遍历，例如dp[7]=max(dp[7],dp[7-weights[i]])，如果你从前向后遍历的话，会先改变dp[7-weights[i]]，但我们需要的是上一轮的结果，所以总结起来就是避免一件物品被取多次；
/ 如果是完全背包，由于每件物品都可以取无限多次，因此必须由前向后遍历。一般背包问题如果没有进行状态压缩的话，顺序是随意的，你从中间向两边都行


*/
var one_dimension_bag_problem = function (
    weights,
    values,
    bagWeight
) {
    let dp = new Array(bagWeight + 1).fill(0);

    for (let itemIdx = 0; itemIdx < weights.length; itemIdx++) {
        for (
            let capacity = bagWeight;
            capacity >= weights[itemIdx];
            capacity--
        ) {
            dp[capacity] = Math.max(
                dp[capacity],
                dp[capacity - weights[itemIdx]] + values[itemIdx]
            );
        }
    }

    console.log(dp);
    return dp[bagWeight];
};

const weights = [1, 3, 4];
const values = [15, 20, 30];
const bagWeight = 4;
let maxValue = one_dimension_bag_problem(weights, values, bagWeight);
console.log(maxValue);
