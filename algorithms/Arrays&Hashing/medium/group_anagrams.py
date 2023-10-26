from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        main_hashmap = defaultdict(list)
        for word in strs:
            abc_list = [0] * 26
            for letter in word:
                abc_list[ord(letter) - ord("a")] += 1
            main_hashmap[tuple(abc_list)].append(word)
        return list(main_hashmap.values())


inst = Solution()
res = inst.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(res)
