// todo: 早上做
var reverseWords = function (s) {
    let strArr = s.split("");
    let startIdx = 0;
    let endIdx = removeExtraSpace(strArr);
    reverseString(strArr, startIdx, endIdx);
    // let newStr = strArr.join("").slice(startIdx, endIdx + 1);
    console.log(strArr.slice(startIdx, endIdx + 1));
    let wordStartIdx = 0;
    for (let i = 0; i < endIdx + 1; i++) {
        if (strArr[i] === " ") {
            console.log(wordStartIdx, i);
            reverseString(strArr, wordStartIdx, i - 1);
            wordStartIdx = i + 1;
        }
    }
    reverseString(strArr, wordStartIdx, endIdx);
    newStr = strArr.join("").slice(startIdx, endIdx + 1);
    // console.log(`"${newStr}"`);
    return newStr;
};

function removeExtraSpace(strArr) {
    let left = 0;
    let right = 0;
    // # 消除leading zeros
    while (strArr[right] === " " && right < strArr.length) {
        right++;
    }

    // # 将字符串复写进入slow 开始的位置直到结束(这其中要考虑单词间的spaces)
    while (right < strArr.length) {
        if (strArr[right] !== " ") {
            strArr[left] = strArr[right];
            left++;
            right++;
        } else {
            if (right > 0 && strArr[right - 1] !== " ") {
                strArr[left] = strArr[right];
                left++;
                right++;
            } else {
                right++;
            }
        }
    }

    if (left > 0 && strArr[left - 1] === " ") return left - 2;
    return left - 1;
}

function reverseString(strArr, left, right) {
    while (left < right) {
        [strArr[left], strArr[right]] = [strArr[right], strArr[left]];
        left++;
        right--;
    }
}

reverseWords("   hello    world !    ");
