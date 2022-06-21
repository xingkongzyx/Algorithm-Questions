    var lastStoneWeightII = function (stones) {
        let totalWeight = 0;
        for (let stoneWeight of stones) {
            totalWeight += stoneWeight;
        }
        let bagWeight = Math.floor(totalWeight / 2);
        let dp = new Array(bagWeight + 1).fill(0);

        for (let itemIdx = 0; itemIdx < stones.length; itemIdx++) {
            for (
                let capacity = bagWeight;
                capacity >= stones[itemIdx];
                capacity--
            ) {
                dp[capacity] = Math.max(
                    dp[capacity],
                    dp[capacity - stones[itemIdx]] + stones[itemIdx]
                );
            }
        }

        //# 在计算 bagWeight bagWeight = totalWeight / 2, 因为是向下取整，所以 totalWeight - firstPart; 一定是大于等于dp[bagWeight]的。
        let firstPart = dp[bagWeight];
        let secondPart = totalWeight - firstPart;
        return secondPart - firstPart;
    };
