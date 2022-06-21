// https://leetcode-cn.com/problems/koko-eating-bananas/solution/bu-yao-shang-lai-jiu-gao-su-wo-shi-er-fe-8n1y/

var minEatingSpeed = function (piles, h) {
    // 最小值是每小时吃一根香蕉,最大值是每小时吃 piles数组中最多根数的香蕉数
    // 计算堆中香蕉最大值

    // 速度最小的时候，耗时最长
    let low = 1;
    // 速度最大的时候，耗时最短
    let high = Math.max(...piles);

    while (low <= high) {
        let mid = Math.floor((low + high) / 2);
        if (calculateTime(piles, mid) > h) {
            // 耗时太多，说明速度太慢了，需要吃比mid数量更多的香蕉, 所以low = mid + 1
            low = mid + 1;
        } else {
            // 如果时间足够或者时间 < h,则说明目前吃的香蕉绰绰有余,我们要修改right从而找到最小的满足时间的香蕉根数
            high = mid - 1;
        }
    }
    return low;
};

const calculateTime = (piles, speed) => {
    let times = 0;
    for (let pile of piles) {
        // 向上取整
        times += Math.ceil(pile / speed);
    }
    return times;
};
