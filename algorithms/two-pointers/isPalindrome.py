"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing
all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.


Example 1:
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.

Example 3:
    Input: s = " "
    Output: true
    Explanation: s is an empty string "" after removing non-alphanumeric characters.
    Since an empty string reads the same forward and backward, it is a palindrome.

"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.lower()
        l_pointer = 0
        r_pointer = len(string) - 1
        while l_pointer < r_pointer:
            if not string[l_pointer].isalnum():
                l_pointer += 1

                continue
            if not string[r_pointer].isalnum():
                r_pointer -= 1
                continue
            if string[l_pointer] != string[r_pointer]:
                return False
            l_pointer += 1
            r_pointer -= 1
        return True


if __name__ == "__main__":

    s = Solution()
    print(s.isPalindrome("f faf af f"))
