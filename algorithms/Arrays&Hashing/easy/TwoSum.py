from typing import List


# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
#
#
#
# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
#
# Input: nums = [3,3], target = 6
# Output: [0,1]




my_list = [5, 2, 8, 1, 9]
my_list2 = [2, 7, 11, 15]
my_list3 = [0, 4, 3, 0]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_dict = {}
        for i, current_num in enumerate(nums):
            num = target - current_num
            num_in_dict = index_dict.get(num, None)
            if isinstance(num_in_dict, int):
                return [i, index_dict[num]]
            else:
                index_dict[current_num] = i


x = Solution()

res1 = x.twoSum(nums=my_list, target=3)
res2 = x.twoSum(nums=my_list2, target=9)
res3 = x.twoSum(nums=my_list3, target=0)
print(res1)
print(res2)
print(res3)
