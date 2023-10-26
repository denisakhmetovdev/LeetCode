from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        # count_list = [[] for _ in range(len(nums) + 1)]
        count_list = [[]] * len(nums)
        print(count_list)
        for num in nums:
            count_dict[num] = 1 + count_dict.get(num, 0)
        for key, value in count_dict.items():
            count_list[value].append(key)

        res = []
        for i in range(len(count_list) - 1, 0, -1):
            for n in count_list[i]:
                res.append(n)
                if len(res) == k:
                    return res


inst = Solution()
print(inst.topKFrequent([0, 0, 1, 1, 1, 3, 3, 4, 5, 5], 4))
print(inst.topKFrequent([], 0))
