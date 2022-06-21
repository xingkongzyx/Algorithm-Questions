/* 
? 通过题意，寻找两数组是否有相同项，并且提示中说可以不要求交集的顺序。
? 
? 既然如此，我们便可以先行将数组排序，方便我们查找，然后正式流程如下：
? 
? 创建一个指针 i 指向 nums1 数组首位，指针 j 指向 nums2 数组首位。
? 创建一个临时栈，用于存放结果集。
? 开始比较指针 i 和指针 j 的值大小，若两个值不等，则数字小的指针，往右移一位。
? 若指针 i 和指针 j 的值相等，则将交集压入栈。
? 若 nums1 或 nums2 有一方遍历结束，代表另一方的剩余值，都是唯一存在，且不会与之产生交集的。
? https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/solution/ha-xi-biao-liang-ge-shu-zu-de-jiao-ji-ii-fkwo/
*/

let intersect = function (nums1, nums2) {
    nums1.sort((a, b) => a - b);
    nums2.sort((a, b) => a - b);
    let l = 0,
        r = 0,
        ans = [];
    while (l < nums1.length && r < nums2.length) {
        if (nums1[l] === nums2[r]) {
            ans.push(nums1[l]);
            l++;
            r++;
        } else nums1[l] < nums2[r] ? l++ : r++;
    }
    // console.log(ans);
    return ans;
};
intersect([1, 1, 2, 2], [2, 2]);
//
