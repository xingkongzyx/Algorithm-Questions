// ! 属于左右指针题目 不能够进行
var isPalindrome = (s) => {
    // 一左一右两个指针相向而行
    let left = 0;
    let right = s.length;
    while (left < right) {
        if (s[left] !== s[right]) return false;
        left++;
        right--;
    }
    return true;
};
