class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            s_dict = {}
            t_dict = {}
            for i in range(len(s)):
                if s_dict.get(s[i], None):
                    s_dict[s[i]] += 1
                else:
                    s_dict[s[i]] = 1
                if t_dict.get(t[i], None):
                    t_dict[t[i]] += 1
                else:
                    t_dict[t[i]] = 1
        return s_dict == t_dict


inst = Solution()
res1 = inst.isAnagram("anagram", "nagaram")
res2 = inst.isAnagram("anagram", "nagarams")
res3 = inst.isAnagram("anagram", "nagaras")
print(res1)
print(res2)
print(res3)
