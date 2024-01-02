// ! 同 219
var numOfSubarrays = function (arr, k, threshold) {
    // 记录当前 size 为 k 的窗口的所有元素的和
    let windowSum = 0;
    let count = 0;
    for (let i = 0; i < arr.length; i++) {
        // 如果当前窗口超出了 size k，移除最左边的元素
        if (i >= k) {
            windowSum -= arr[i - k];
        }

        // 将当前元素的值添加进窗口
        windowSum += arr[i];

        // 判断当前窗口的平均值是否满足要求
        if (i >= k - 1 && windowSum / k >= threshold) {
            console.log("window is from", i - k + 1, "to ", i);
            count++;
        }
    }

    return count;
};

// 标准写法
var numOfSubarrays = function (arr, k, threshold) {
    let windowSum = 0;
    let count = 0;
    let left = 0;
    let right = 0;

    while (right < arr.length) {
        windowSum += arr[right];

        if (right - left + 1 === k) {
            if (windowSum / k >= threshold) {
                count++;
            }
            windowSum -= arr[left];
            left++;
        }

        right++;
    }
    return count;
};
