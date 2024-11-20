from typing import List
from collections import  defaultdict


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        temp_dict = defaultdict(list)
        for idx, number in nums:
            temp_dict[number].append(idx)
        left = 0
        right = len(nums) -1
        while left < right:
            half_total = nums[left] + nums[right]
            if half_total == 0:
                if 0 in temp_dict:
                    result.append([nums[left], 0, nums[right]])
            else:
                if 0 - half_total in temp_dict:
                    res

