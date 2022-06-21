//! 滑动窗口 + 数组
/* 
* 我们先统计出字符串 p 中每个字符的词频数，再把 p 的长度作为滑动窗口的宽度，把这个窗口在字符串 s 中移动，统计窗口中的词频数，如果在移动的过程中，窗口中的词频数与 p 的词频数相等，那么，这个窗口就是 p 的一个异位词。

* 时间复杂度：O(m + (m - n) * C)，m 为总的遍历次数，C 固定为 26，窗口个数为 (m−n+1)，每个窗口都要做字符串比较，比较的时间复杂度为O(C)，所以，去掉常数项，总的时间复杂度为 O(m + (m - n) * C)

?链接：https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/solution/tong-ge-lai-shua-ti-la-hua-dong-chuang-k-xgkv/



*/

var findAnagrams = function (s, p) {
    let result = [];
    let pmap = {};
    let smap = {};
    let lenOfPstr = p.length;
    let lenOfSstr = s.length;
    for (let char of p) {
        if (char in pmap) {
            pmap[char] += 1;
        } else {
            pmap[char] = 1;
        }
    }

    for (let i = 0; i < lenOfPstr; i++) {
        let char = s[i];
        if (char in smap) smap[char] += 1;
        else smap[char] = 1;
    }

    // 若 smap 和 pmap 相等，则找到第一个异位词索引 0
    if (checkTwoMaps(smap, pmap)) result.push(0);

    // *继续遍历s字符串索引为[lenOfSstr, lenOfPstr)的字母，在 smap 中每次增加一个新字母，去除一个旧字母
    // 下面是sliding window的步骤，从 j=lenOfPstr 起步。注意我们j永远指的是新的window的right border. 首先了解一点在新的window之前的起始window是[j - lenOfPstr, j - 1],并且这个window下的关于smap和pmap是否相等我们已经检查过了。所以我们要移动原来的 [j - lenOfPstr, j - 1] window 到 [j - lenOfPstr + 1, j] window, 然后判断 pmap 和更新后的 smap 是否相等，相等则在返回值result中新增异位词索引 (j - lenOfPstr + 1)
    // !移动window的方法就是 首先缩小左侧边界：smap[s[j-lenOfPstr]]的值减1，然后延申右侧边界：此时右侧边界对应的character是smap[j]
    for (let j = lenOfPstr; j < lenOfSstr; j++) {
        let leftChar = s[j - lenOfPstr];
        smap[leftChar] -= 1;
        if (smap[leftChar] === 0) delete smap[leftChar];
        let rightChar = s[j];
        if (smap.hasOwnProperty(rightChar)) smap[rightChar] += 1;
        else smap[rightChar] = 1;
        // 在每次移动完window后我们都要检查当前的window是否满足条件，满足的话把当前window的起始left border(j - lenOfPstr + 1)添加进result

        if (checkTwoMaps(smap, pmap)) result.push(j - lenOfPstr + 1);
    }
    // console.log(result);
    return result;
};

function checkTwoMaps(smap, pmap) {
    for (let keyInSmap in smap) {
        let valInSmap = smap[keyInSmap];
        if (
            pmap.hasOwnProperty(keyInSmap) &&
            pmap[keyInSmap] === valInSmap
        ) {
            continue;
        } else {
            return false;
        }
    }
    return true;
}
// findAnagrams("cbaebabacd", "abc");
