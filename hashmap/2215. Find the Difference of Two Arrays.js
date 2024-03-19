/* 
/ 时间复杂度：O(n1+n2)，其中 n1 ​与 n2​ 分别为数组 nums1 ​和 nums2 ​的长度。维护两数组元素对应哈希集合与遍历计算答案的时间复杂度均为 O(n1+n2)。空间复杂度：O(n1+n2)，即为两数组元素对应哈希集合的空间开销。 作者：力扣官方题解 
? 链接：https://leetcode.cn/problems/find-the-difference-of-two-arrays/solutions/1379222/zhao-chu-liang-shu-zu-de-bu-tong-by-leet-78u0/
*/
var findDifference = function (nums1, nums2) {
    let nums1Set = new Set(nums1);
    let nums2Set = new Set(nums2);

    let ans0 = [];
    let ans1 = [];

    for (let num of nums1Set) {
        if (!nums2Set.has(num)) {
            ans0.push(num);
        }
    }

    for (let num of nums2Set) {
        if (!nums1Set.has(num)) {
            ans1.push(num);
        }
    }
    return [ans0, ans1];
};
