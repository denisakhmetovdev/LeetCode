"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.



Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]


Constraints:

1 <= nums.length <= 10^5
-2^31 <= nums[i] <= 2^31 - 1
0 <= k <= 10^5


Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?

--------------------------------------------------
Дан целочисленный массив nums. Поверните массив вправо на k шагов, где k — неотрицательное число.


Пример 1:
Ввод: nums = [1,2,3,4,5,6,7], k = 3
 Вывод: [5,6,7,1,2,3,4]
 Объяснение:
поворот на 1 шаг вправо: [7,1,2,3,4,5,6]
поворот на 2 шага вправо: [6,7,1,2,3,4,5]
поворот на 3 шага вправо: [5,6,7,1,2,3,4]

Пример 2:
Ввод: nums = [-1,-100,3,99], k = 2
 Вывод: [3,99,-1,-100]
 Пояснение:
поворот на 1 шаг вправо: [99,-1,-100,3]
поворот на 2 шага вправо: [3,99,-1,-100]


Ограничения:

1 <= nums.length <= 10^5
-2^31 <= nums[i] <= 2^31 - 1
0 <= k <= 10^5


Ограничения:
Попробуйте придумать как можно больше решений. Существует как минимум три разных способа решить эту проблему.
Можно ли сделать это на месте, оставив O(1)дополнительное пространство?
"""


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Временная сложность O(n)
        Пространственная сложность O(n)
        """
        if len(nums) < 2:
            return
        k %= len(nums)
        if k == 0:
            return
        nums[:] = nums[-k:] + nums[:-k]

    def rotate2(self, nums: list[int], k: int) -> None:
        """
        Почти то же самое, что и self.rotate()
        Временная сложность O(n)
        Пространственная сложность O(n)
        """
        if len(nums) < 2:
            return
        k %= len(nums)
        if k == 0:
            return
        length = len(nums[:-k])
        for i in range(length):
            nums.append(nums[i])
        nums[:] = nums[length:]

    def rotate3(self, nums: list[int], k: int) -> None:
        """
        Временная сложность O(n)
        Пространственная сложность O(n)
        -- Создаётся временный массив
        """
        temp_nums = nums[:]
        length = len(temp_nums)
        for i in range(len(nums)):
            new_position = (i + length - k) % length
            nums[i] = temp_nums[new_position]

    def rotate4(self, nums: list[int], k: int) -> None:
        """
        Временная сложность O(n)
        Пространственная сложность O(1)
        """
        length = len(nums)
        k %= length
        nums.reverse()  # Переворачиваем весь список
        nums[:k] = reversed(nums[:k])  # Переворачиваем первые k элементов
        nums[k:] = reversed(nums[k:])  # Переворачиваем оставшиеся элементы


if __name__ == '__main__':
    s = Solution()
    l = [1, 2, 3, 4, 5, 6, 7]
    l_copy = l[:]
    m = [1, 2, 3, 4, 5, 6, 7]
    m_copy = m[:]
    n = [1, 2, 3, 4, 5, 6, 7]
    n_copy = n[:]
    o = [1, 2, 3, 4, 5, 6, 7]
    o_copy = o[:]
    # print(f"o = {o}")
    s.rotate(l, 3)
    s.rotate2(m, 3)
    s.rotate3(n, 3)
    s.rotate4(o, 3)
    print(" rotate()::: ", l_copy, " | ", l)
    print("rotate2()::: ", m_copy, " | ", m)
    print("rotate3()::: ", n_copy, " | ", n)
    print("rotate4()::: ", o_copy, " | ", o)
