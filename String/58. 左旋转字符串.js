/* 
!这道题目与 151 也非常类似，依然可以通过局部反转+整体反转 达到左旋转的目的。

*具体步骤为：
*
*先翻转整个字符串
*再局部反转 [0, strInArr.length - n - 1]
*最后反转[strInArr.length - n, strInArr.length - 1]
*最后就可以得到左旋n的目的，而不用定义新的字符串，完全在本串上操作。
*/

var reverseLeftWords = function (s, n) {
    let strInArr = s.split("");
    // 先翻转整个字符串
    reverseString(strInArr, 0, strInArr.length - 1);
    // 再局部反转 [0, strInArr.length - n - 1] 以及 [strInArr.length - n, strInArr.length - 1]
    reverseString(strInArr, 0, strInArr.length - n - 1);
    reverseString(strInArr, strInArr.length - n, strInArr.length - 1);
    console.log(strInArr.join(""));
};

function reverseString(str, left, right) {
    while (left < right) {
        [str[left], str[right]] = [str[right], str[left]];
        left++;
        right--;
    }
}

let s = "abcdefg";
let k = 2;
reverseLeftWords(s, k);
