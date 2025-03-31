/* 
https://leetcode.cn/problems/pancake-sorting/solutions/1275857/fu-xue-ming-zhu-tu-jie-jian-bing-pai-xu-jto8z
https://leetcode.cn/problems/pancake-sorting/solutions/1275785/gong-shui-san-xie-mou-pao-pai-xu-yun-yon-c0mn

      * 翻转排序策略：
      * 1、找出下标范围[0, index]内的最大值 curLargestNum 的下标 idx
      * 2、使 k = idx + 1, 然后进行煎饼翻转，操作完成后，arr[0] 是 [0, index] 范围内的最大值
      * 3、使 k = index + 1, 然后进行煎饼翻转，操作完成后，arr[index] 是 [0, index] 范围内的最大值
      * 4、将 index 减一，然后重复 1、2、3 操作；当 index = 0 时，直接返回（终止条件）

*/

/**
 * @param {number[]} arr
 * @return {number[]}
 */
var pancakeSort = function (arr) {
    const res = [];
    let sortedEle = 0;
    for (
        let curLargestNum = arr.length;
        curLargestNum > 0;
        curLargestNum--
    ) {
        let idx = 0;
        while (idx < arr.length && arr[idx] !== curLargestNum) {
            idx++;
        }

        res.push(idx + 1);
        reverseArr(arr, 0, idx);
        // console.log('1', arr)
        res.push(arr.length - sortedEle);
        reverseArr(arr, 0, arr.length - sortedEle - 1);
        // console.log('2', arr)
        sortedEle++;
    }
    return res;
};

function reverseArr(arr, left, right) {
    while (left < right) {
        let temp = arr[left];
        arr[left] = arr[right];
        arr[right] = temp;
        left++;
        right--;
    }
}
