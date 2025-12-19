// https://leetcode-cn.com/problems/gas-station/solution/jia-you-zhan-by-19216801-rt1i/
// https://leetcode-cn.com/problems/gas-station/solution/shi-yong-tu-de-si-xiang-fen-xi-gai-wen-ti-by-cyayc/
// ! 这道题更多是理解，而非是严格的贪心算法
/* 
我研究了一整天这个题解终于理解了，提供一个思路：

首先判断总gas能不能大于等于总cost，如果总gas不够，一切都白搭对吧（总（gas- cost）不用单独去计算，和找最低点时一起计算即可，只遍历一次）；

再就是找总（gas-cost）的最低点，不管正负（当然如果最低点都是正的话那肯定能跑完了）；

找到最低点后，如果有解，那么解就是最低点的下一个点，因为总（gas-cost）是大于等于0的，所以前面损失的gas我从最低点下一个点开始都会拿回来！（此处@小马哥！“我要争一口气，不是想证明我了不起。我是要告诉人家，我失去的东西一定要拿回来！”），别管后面的趋势是先加后减还是先减后加，最终结果我是能填平前面的坑的。
*/
var canCompleteCircuit = function (gas, cost) {
    let minGas = Infinity;
    let minIndex = 0;
    let currentGas = 0;
    for (let i = 0; i < gas.length; i++) {
        //# 走过了第i段路后邮箱里的油
        currentGas = currentGas + gas[i] - cost[i];
        if (currentGas < minGas) {
            minGas = currentGas;
            minIndex = i;
        }
    }

    if (currentGas < 0) return -1;
    //# 为什么要加1，假设第一次遍历的时候就直接找到了 minGas, minIndex. 我们知道此时的i虽然为0但是实际上 currentGas 是经过第0个站点的加油并走过了第0段路到达的第一个站点(也是index为1的站点)时的油量，如果他是最小值根据理论我们的结果应该是1，因为到达第一个站点时剩余油量最小。而此时i=0, 所以我们必须返回 (i+1) 也就是 (minIndex+1).

    //# 进行 % gas.length 的原因是如果当  i===gas.length-1 时得到了新的 minGas 和 minIndex，说明此时是到达了或者说又返回了起始位置(index 0的站点)，并且在这个位置油量最少。所以我们应该从这个位置出发，按照我们上面的理论 - minIndex + 1 = gas.length - 1 + 1 - 结果是 gas.length, 是超出边界的值，我们想要得到的是0. 如果 % gas.length，结果是0，也正好是我们要的起始位置。这就是最后的结果要进行 % gas.length 的原因。
    return (minIndex + 1) % gas.length;
};
