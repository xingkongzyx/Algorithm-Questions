/* 
https://leetcode.com/problems/longest-mountain-in-array/solutions/1215470/c-easy-solution-with-comments-and-algorithm/

由于在一次「从峰顶展开」的过程中，每个元素在最坏情况下也只可能被访问或比较两次（一次在向左扩展时，另一次在向右扩展时），并且在完成一次扩展后，外层循环的 i 会直接跳到 end_root，从而避免了重复扫描。(关键点在于，展开之后会把 i 更新为 toRight - 1：i = toRight - 1; 这样可以确保下次外层 for 循环迭代时，我们跳过了已经展开过的部分，不会再次冗余地向左或向右重复扫描。)
因此，总的来看每个元素都不会被重复地「深入扫描」多次，所以整体算法的时间复杂度是 O(n)。
*/
var longestMountain = function (arr) {
    let maxLen = 0;
    for (let i = 1; i < arr.length - 1; i++) {
        if (arr[i] > arr[i - 1] && arr[i] > arr[i + 1]) {
            let toLeft = i - 1;
            let toRight = i + 1;
            let curLen = 1;
            while (toLeft >= 0 && arr[toLeft] < arr[toLeft + 1]) {
                curLen++;
                toLeft--;
            }
            while (
                toRight <= arr.length - 1 &&
                arr[toRight] < arr[toRight - 1]
            ) {
                curLen++;
                toRight++;
            }
            // console.log("i", i, "toleft", toLeft, "toright", toRight, "curlen", curLen)
            maxLen = Math.max(curLen, maxLen);
            i = toRight - 1;
        }
        // console.log("i---", i)
    }

    return maxLen;
};
