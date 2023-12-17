/* 
https://www.programmercarl.com/0042.%E6%8E%A5%E9%9B%A8%E6%B0%B4.html#%E6%80%9D%E8%B7%AF
/ 时间复杂度: O(n)。
/ 空间复杂度: O(n)，用来保存每一列左边最高的墙和右边最高的墙。
为了得到两边的最高高度，使用了双指针来遍历，每到一个柱子都向两边遍历一遍，这其实是有重复计算的。我们把每一个位置的左边最高高度记录在一个数组上（maxLeft），右边最高高度记录在一个数组上（maxRight），这样就避免了重复计算。

当前位置，左边的最高高度是前一个位置的左边最高高度和本高度的最大值。

从左向右遍历：maxLeft[i] = max(height[i], maxLeft[i - 1]);
从右向左遍历：maxRight[i] = max(height[i], maxRight[i + 1]);

*/
function trap(height) {
    if (height.length <= 2) return 0;

    let maxLeft = new Array(height.length).fill(0);
    let maxRight = new Array(height.length).fill(0);
    let size = height.length;

    // Record the maximum height to the left of each bar
    maxLeft[0] = height[0];
    for (let i = 1; i < size; i++) {
        maxLeft[i] = Math.max(height[i], maxLeft[i - 1]);
    }

    // Record the maximum height to the right of each bar
    maxRight[size - 1] = height[size - 1];
    for (let i = size - 2; i >= 0; i--) {
        maxRight[i] = Math.max(height[i], maxRight[i + 1]);
    }

    // Calculate the total water trapped
    let sum = 0;
    for (let i = 0; i < size; i++) {
        // 这里 Math.min 的结果是有可能等于 height[i], 因为我们高度数组的计算方法为了省事是包含当前元素的，所以要判断 count 是否大于 0
        let count = Math.min(maxLeft[i], maxRight[i]) - height[i];
        if (count > 0) sum += count;
    }

    return sum;
}

print(Solution().trap((height = [4, 2, 0, 3, 2, 5])));
