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

        console.log(left, right, "windowSum", windowSum);
    }
    return count;
};

numOfSubarrays([2, 2, 2, 2, 5, 5, 5, 8], 3, 4);
