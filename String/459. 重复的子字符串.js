// ! KMP经典题型

/* 
# 我直接先来说下公式：
# len(s) % (len(s) -  maxLen) = 0
# 其中 len(s) 为字符串 s 的长度，maxLen 为最长公共前后缀的长度。
# 所以这个公式翻译一下就是：如果 s 是周期串，那【s 的长度】是【s 的长度减去最长公共前后缀的长度】的倍数，那字符串 s 就是周期串。

作者：编程文青李狗蛋
链接：https://juejin.cn/post/7069189334787686437
*/

function repeatedSubstringPattern(s) {
    const patternList = buildPatternList(s);
    let len = s.length;
    /*
    ?      a    s    d   a   s   d   a   s   d
    ?     -1   -1   -1   0   1   2   3   4   5     patternList数组

      * 我们可以看出如果s是由子串重复构成的话，会从第二个子串开始有最长相等前后缀，并且len - 6 (6是由(len-patternList[pattern.len-1]计算) 就是一个字串的长度 也是第一个字串
      * 如果这个长度可以被整除，就说明整个字符串就是这个周期的循环。
    */

    if (
        patternList[patternList.length - 1] !== -1 &&
        len % (len - patternList[patternList.length - 1] - 1) === 0
    )
        return true;

    return false;
}

function buildPatternList(str) {
    let list = new Array(str.length).fill(-1);

    if (list.length < 2) return list;

    let traversePointer = 1;
    let j = 0;
    while (traversePointer < list.length) {
        if (str[traversePointer] === str[j]) {
            list[traversePointer] = j;
            traversePointer++;
            j++;
        } else if (j > 0) {
            //# 如果此时j在一个pattern的匹配之中意味着j>0则我们判断前面是否还有一样的pattern。我们通过 list[j-1] 寻找上个pattern。如果没有则 list[j-1] = -1. j再加1变为0. 这时我们没有更新i，我们交给下一轮while loop判断新的 str[j] 是否与 str[traversePointer] 相等。或者此时j已经是0，意味着没有任何对应的pattern，我们只需要更新 traversePointer,看看新的位置是否有pattern
            j = list[j - 1] + 1;
        } else if (j === 0) {
            traversePointer++;
        }
    }
    return list;
}

let haystack = "asdasdasd";

console.log(strStr(haystack));
