class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_int = str(x)
        small_pointer = 0
        big_pointer = len(str_int) - 1
        while small_pointer < big_pointer:
            if str_int[small_pointer] != str_int[big_pointer]:
                return False
            small_pointer += 1
            big_pointer -= 1
        return True


s = Solution()
res = s.isPalindrome(11211)
print(res)
