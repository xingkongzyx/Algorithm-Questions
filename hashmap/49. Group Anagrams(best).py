""" 
* 由于互为字母异位词的两个字符串包含的字母相同，因此两个字符串中的相同字母出现的次数一定是相同的，故可以将每个字母出现的次数使用字符串表示，作为哈希表的键。

* 由于字符串只包含小写字母，因此对于每个字符串，可以使用长度为 2626 的数组记录每个字母出现的次数。需要注意的是，在使用数组作为哈希表的键时，不同语言的支持程度不同，因此不同语言的实现方式也不同。
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
