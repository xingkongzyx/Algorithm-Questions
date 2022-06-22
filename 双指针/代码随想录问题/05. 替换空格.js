/**
 * @param {string} s
 * @return {string}
 */
var replaceSpace = function (s) {
    let strInArr = s.split("");
    let oldLen = strInArr.length;
    let space = 0;
    for (let char of strInArr) {
        if (char == " ") space += 1;
    }
    if (space === 0) return s;

    let newLen = oldLen + space * 2;
    //* 因为index是从0起始的, 所以 left, right pointers 的起始位置都是 length-1
    //* right比left领先的几个spaces 都是每个 " " 替换为 "%20" 多出来的位置，当左右指针相遇则说明所有 spaces 已经处理完毕。
    let left = oldLen - 1;
    let right = newLen - 1;
    while (left < right) {
        if (strInArr[left] !== " ") {
            strInArr[right] = strInArr[left];
            left--;
            right--;
        } else {
            strInArr[right] = "0";
            strInArr[right - 1] = "2";
            strInArr[right - 2] = "%";
            left--;
            right -= 3;
        }
    }

    return strInArr.join("");
};
