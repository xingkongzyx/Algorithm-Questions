//? https://leetcode.cn/problems/permutation-sequence/solution/shou-hua-tu-jie-jing-dian-de-dfshui-su-shu-xue-gui/
/// 时间复杂度：O(n^2)
const getPermutation = (n, k) => {
    //# 代码以「n = 4, k = 10」为例
    //* nums 存储从 1 到 n 的所有元素, 用于在后续步骤中直接锁定第 k 个位置
    const nums = [];
    //* factorial 等于「n个数」的全排列「数量」一共有多少个
    let factorial = 1;

    for (let i = 1; i <= n; i++) {
        nums.push(i); // [1, 2, 3, 4]
        factorial = factorial * i; // 4!   24
    }

    //* nums中数字们的索引是从0开始, 所以k要先减去1
    k--;
    let resStr = "";

    while (nums.length > 0) {
        //* 以「n = 4, k = 10」为例, 相当于先计算出全排列中以当前「nums 数组中的每个元素」为首位(比如说1为首位, 2为首位, 3为首位, 4为首位)的各自的排列个数。这里就是 6. 然后通过计算 index 获得 k 应该是落在哪个首位上, 最后通过 nums[index] 获取对应的数字。
        factorial = factorial / nums.length;
        const index = (k / factorial) | 0;
        //* 加上当前选的数字
        resStr += nums[index];
        //* nums删去选的这个数字, 因为后面的位置不可能再用到同一个数字, 直到 nums 为空, 退出循环
        nums.splice(index, 1);
        //* 更新 k
        k = k % factorial;
    }
    return resStr;
};
