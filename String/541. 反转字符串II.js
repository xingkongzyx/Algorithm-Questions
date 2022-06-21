var reverseStr = function (s, k) {
    let strInArr = s.split("");
    for (let i = 0; i < strInArr.length; i += 2 * k) {
        //* 在这个区间内，如果前K个字符还在 strInArr 的范围内，则对其进行颠倒
        if (i + k < strInArr.length) {
            reverseHelper(strInArr, i, i + k - 1);
        } else {
            //* 在这个区间内，如果前K个字符已经超过了 strInArr 的范围内，则对剩下的从i开始的所有字符进行颠倒
            reverseHelper(strInArr, i, strInArr.length - 1);
        }
    }
    return strInArr.join("");
};

var reverseHelper = function (s, left, right) {
    while (left < right) {
        [s[left], s[right]] = [s[right], s[left]];
        left++;
        right--;
    }
};

let s = "abcdefgt";
let k = 2;
reverseStr(s, k);
