/* 
*1.采用分为两组，HashMap 存一组，另一组和 HashMap 进行比对。
*2.这样的话情况就可以分为三种：
*     HashMap 存一个数组，如 A。然后计算三个数组之和，如 BCD。时间复杂度为：O(n)+O(n^3)，得到 O(n^3).
*     HashMap 存三个数组之和，如 ABC。然后计算一个数组，如 D。时间复杂度为：O(n^3)+O(n)，得到 O(n^3).
*     HashMap存两个数组之和，如AB。然后计算两个数组之和，如 CD。时间复杂度为：O(n^2)+O(n^2)，得到 O(n^2).
*3.根据第二点我们可以得出要存两个数组算两个数组。
*4.我们以存 AB 两数组之和为例。首先求出 A 和 B 任意两数之和 sumAB，以 sumAB 为 key，sumAB 出现的次数为 value，存入 hashmap 中。然后计算 C 和 D 中任意两数之和的相反数 sumCD，在 hashmap 中查找是否存在 key 为 sumCD。

!算法时间复杂度为 O(n^2)。
链接：https://leetcode-cn.com/problems/4sum-ii/solution/chao-ji-rong-yi-li-jie-de-fang-fa-si-shu-xiang-jia/

*/

var fourSumCount = function (nums1, nums2, nums3, nums4) {
    let mapOfSumOfnums1Andnums2 = {};
    let times = 0;
    for (let numFromNums1 of nums1) {
        for (let numFromNums2 of nums2) {
            let sum = numFromNums1 + numFromNums2;
            mapOfSumOfnums1Andnums2.hasOwnProperty(sum)
                ? (mapOfSumOfnums1Andnums2[sum] += 1)
                : (mapOfSumOfnums1Andnums2[sum] = 1);
        }
    }

    for (let numFromNums3 of nums3) {
        for (let numFromNums4 of nums4) {
            let sum = numFromNums3 + numFromNums4;
            let foundNum = 0 - sum;
            if (mapOfSumOfnums1Andnums2.hasOwnProperty(foundNum))
                times += mapOfSumOfnums1Andnums2[foundNum];
        }
    }
    // console.log(times);
    // console.log(mapOfSumOfnums1Andnums2);
    return times;
};
const nums1 = [-1, -1];
const nums2 = [-1, 1];
const nums3 = [-1, 1];
const nums4 = [1, -1];
fourSumCount(nums1, nums2, nums3, nums4);
