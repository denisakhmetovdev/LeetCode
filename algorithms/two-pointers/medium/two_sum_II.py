from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_ptr = 0
        right_ptr = len(numbers) - 1
        while left_ptr < right_ptr:
            total = numbers[left_ptr] + numbers[right_ptr]
            if total == target:
                return [left_ptr + 1, right_ptr + 1]
            if total > target:
                right_ptr -= 1
                continue
            else:
                left_ptr += 1
                continue


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2,7,11,15], target=9))
    print(s.twoSum([2,3,4], target=6))
    print(s.twoSum([-1,0], target=-1))
