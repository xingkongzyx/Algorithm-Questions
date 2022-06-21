var reverseWords = function (s) {
    let strInArr = s.split("");
    let endIdx = removeExtraSpace(strInArr);
    // console.log(strInArr.slice(0, endIdx + 1));
    reverseStrArr(strInArr, 0, endIdx);
    for (let i = 0; i < endIdx + 1; i++) {
        let left = i;
        let right = i;
        while (right < endIdx + 1 && strInArr[right] !== " ") {
            right++;
        }
        i = right;
        reverseStrArr(strInArr, left, right - 1);
    }
    let res = strInArr.slice(0, endIdx + 1).join("");
    // console.log(`"${res}"`);
    return res;
};

function removeExtraSpace(arr) {
    let slow = 0;
    let fast = 0;
    // * 1. 将fast pointer 越过前面的spaces，因为我们要分三种情况消除空格，第一种就是消除最开始的空格
    while (arr[fast] === " ") {
        fast++;
    }

    // * 2. 这时 fast pointer 已经指向了第一个真正的character，我们将fast pointer指向的value replace the value in the slow pointer.
    // !但在这里我们也得判断单词之间的空格
    while (fast < arr.length) {
        if (
            fast - 1 > 0 &&
            arr[fast] === " " &&
            arr[fast - 1] === " "
        ) {
            fast++;
        } else {
            arr[slow] = arr[fast];
            slow++;
            fast++;
        }
    }
    // console.log(arr);
    // * 最后消除末尾的空白字符, 通过纸上画图发现如果末尾没有空格时slow所在的位置比实际数组的末尾位置一位，如果有空白字符，slow所在位置比实际数组的末尾位置多两位并且多的第一位是一个空格
    if (arr[slow - 1] === " ") return slow - 2;
    return slow - 1;
}

function reverseStrArr(arr, left, right) {
    while (left < right) {
        [arr[left], arr[right]] = [arr[right], arr[left]];
        left++;
        right--;
    }
}

reverseWords("I ");
