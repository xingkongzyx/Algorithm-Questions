""" 
/ 时间复杂度: O(nklogk), 其中 n 是 strs 中的字符串的数量, k 是 strs 中的字符串的的最大长度。需要遍历 n 个字符串, 对于每个字符串, 需要 O(klogk) 的时间进行排序以及 O(1) 的时间更新哈希表, 因此总时间复杂度是 O(nklogk)。
/ 空间复杂度: O(nk), 其中 n 是 strs 中的字符串的数量, k 是 strs 中的字符串的的最大长度。需要用哈希表存储全部字符串。

? https://leetcode.cn/problems/group-anagrams/solution/zi-mu-yi-wei-ci-fen-zu-by-leetcode-solut-gyoc/

"""

import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)

        for st in strs:
            key = "".join(sorted(st))
            mp[key].append(st)

        return list(mp.values())
