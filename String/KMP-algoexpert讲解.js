/* 
! KMP的主要思想是当出现字符串不匹配时，可以知道一部分之前已经匹配的文本内容，可以利用这些信息避免从头再去做匹配了。
* Write a function that takes in two strings and checks if the first string contains the second one using the Knuth—Morris—Pratt algorithm. The function should return a boolean.
* 
* If you're unfamiliar with the Knuth—Morris—Pratt Algorithm, we recommend watching the Conceptual Overview section of this question's video explanation before starting to code.
? Sample Input
? string = "aefoaefcdaefcdaed"
? substring = "aefcdaed"

? Sample Output
? true
 */

function knuthMorrisPrattAlgorithm(string, substring) {
    let patternList = buildPatternList(substring);
    let res = doesMatch(string, substring, patternList);
    return res;
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

function doesMatch(string, substring, patternList) {
    // # the pointer to traverse string, and never go back
    let traversePointer = 0;
    // # the pointer to traverse substring, if this character does not match the character in string, it will go back forward to find the pattern
    let j = 0;
    while (traversePointer < string.length) {
        if (string[traversePointer] === substring[j]) {
            traversePointer++;
            j++;
        } else if (j > 0) {
            j = patternList[j - 1] + 1;
        } else if (j === 0) {
            traversePointer++;
        }

        if (j === substring.length) return true;
    }
    return false;
}
