from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_sequence = set(nums)
        res = 0
        for num in unique_sequence:
            if num - 1 not in unique_sequence:
                temp_len = 0
                while num + temp_len in unique_sequence:
                    temp_len += 1
                res = max(temp_len, res)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))
    print(s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
    print(s.longestConsecutive([1, 3, 6]))
