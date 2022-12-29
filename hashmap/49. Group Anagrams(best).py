""" 
* 由于互为字母异位词的两个字符串包含的字母相同, 因此两个字符串中的相同字母出现的次数一定是相同的, 故可以将每个字母出现的次数使用字符串表示, 作为哈希表的键。

* 由于字符串只包含小写字母, 因此对于每个字符串, 可以使用长度为 26 的数组记录每个字母出现的次数。需要注意的是, 在使用数组作为哈希表的键时, 不同语言的支持程度不同, 因此不同语言的实现方式也不同。

/ 时间复杂度: O(n(k+|Σ|)), 其中 n 是 strs 中的字符串的数量, k 是 strs 中的字符串的的最大长度, Σ 是字符集, 在本题中字符集为所有小写字母, |Σ|=26。需要遍历 n 个字符串, 对于每个字符串, 需要 O(k) 的时间计算每个字母出现的次数, O(|Σ|) 的时间生成哈希表的键, 以及 O(1) 的时间更新哈希表, 因此总时间复杂度是 O(n(k+|Σ|))。
/ 空间复杂度: O(n(k+|Σ|)), 其中 n 是 strs 中的字符串的数量, k 是 strs 中的字符串的最大长度, Σ 是字符集, 在本题中字符集为所有小写字母, |Σ|=26。需要用哈希表存储全部字符串, 而记录每个字符串中每个字母出现次数的数组需要的空间为 O(|Σ|), 在渐进意义下小于 O(n(k+|Σ|)), 可以忽略不计。


? https://leetcode.cn/problems/group-anagrams/solution/zi-mu-yi-wei-ci-fen-zu-by-leetcode-solut-gyoc/

 """


class Solution:
    def groupAnagrams(self, strs):
        from collections import defaultdict
        map = defaultdict(list)
        for cur_str in strs:
            counts = [0] * 26
            for char in cur_str:
                counts[ord(char) - ord('a')] += 1

            # ! 需要将 list 转换成 tuple 才能进行哈希
            map[tuple(counts)].append(cur_str)
        return list(map.values())


print(Solution().groupAnagrams(
    strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
