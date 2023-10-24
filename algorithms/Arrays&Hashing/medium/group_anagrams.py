from typing import List

# main_hashmap = {
#     len(word[0]): {index: {}}
#     len(word[1]): {index: {}}
#
# }


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        main_hashmap = {}
        len_strs = len(strs)
        for i, word in enumerate(strs):
            words_dict = {}
            for letter in word:
                words_dict[letter] = 1 + words_dict.get(letter, 0)

            main_hashmap[len(word)] = {i: words_dict}
