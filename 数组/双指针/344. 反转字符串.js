// 属于左右指针题目

var reverseString = function (s) {
    let left = 0;
    let right = s.length - 1;
    while (left < right) {
        [s[left], s[right]] = [s[right], s[left]];
        left++;
        right--;
    }
    console.log(s);
};

reverseString(["h", "e", "l", "l", "o"]);
