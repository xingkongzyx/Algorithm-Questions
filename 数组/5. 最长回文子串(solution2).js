/* 
「中心扩散法」的基本思想是：遍历每一个下标，以这个下标为中心，利用「回文串」中心对称的特点，往两边扩散，看最多能扩散多远。枚举「中心位置」时间复杂度为 O(N)，从「中心位置」扩散得到「回文子串」的时间复杂度为 O(N)，因此时间复杂度可以降到 O(N^2)。

细节：回文串在长度为奇数和偶数的时候，「回文中心」的形态不一样：
  * 奇数回文串的「中心」是一个具体的字符，例如：回文串 "aba" 的中心是字符 "b"；
  * 偶数回文串的「中心」是位于中间的两个字符的「空隙」，例如：回文串 "abba" 的中心是两个 "b"，也可以看成两个 "b" 中间的空隙。
*/
// // dfdf
var longestPalindrome = function (s) {
    // 这里的两个elements是回文串的[leftIdx, rightIdx]. 如果回文串是一个字符 "a".那么这个数组是[0,0]
    let longestPalindrome = [0, 0];
    for (let i = 1; i < s.length; i++) {
        // 遍历s中的每一个位置，然后假设这个位置分别是奇数回文串和偶数回文串的center并根据此求出对应的边界index. 像 "cac" 从index 1 "a"开始遍历。奇数回文串就是以a 为中心检查左右两边的"c", "c".
        // 偶数回文串就是以"a"左边的空隙为中心，下一次要检查的character是 "c" 和 "a"

        // 返回的结果都是如同longestPalindrome = [0, 0]定义的那样。第一个index是回文串的左边，第二个index是回文串的右边
        let odd = getLongestPalindromeFrom(s, i - 1, i + 1);
        let even = getLongestPalindromeFrom(s, i - 1, i);
        console.log("odd is: ", odd);
        console.log("even is: ", even);
        let longestPalindromeInCurrentTern =
            odd[1] - odd[0] > even[1] - even[0] ? odd : even;
        if (
            longestPalindromeInCurrentTern[1] -
                longestPalindromeInCurrentTern[0] +
                1 >
            longestPalindrome[1] - longestPalindrome[0] + 1
        ) {
            longestPalindrome = longestPalindromeInCurrentTern;
        }
    }
    // console.log(longestPalindrome);
    return s.slice(longestPalindrome[0], longestPalindrome[1] + 1);
};

function getLongestPalindromeFrom(str, left, right) {
    while (left >= 0 && right < str.length) {
        if (str[left] !== str[right]) break;
        left--;
        right++;
    }
    return [left + 1, right - 1];
}

// longestPalindrome("cbbd");
console.log(longestPalindrome("abaxyzzyxf"));
