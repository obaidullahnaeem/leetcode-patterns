###  4 pillars of oop 1 encapculation 2 inheritance 3 polymorphism 4 abstraction
### methodoverload , overrride

# 9. Palindrome Number
from more_itertools import strip


class Solution(object):
    @classmethod
    def isPalindrome(self, x):
        if x<0: return False
        x=str(x)
        if len(x) <= 1 : return True
        if x[0] == x[-1]:
            return self.isPalindrome(str(x)[1:-1])
        else: return False
# Solution.isPalindrome(121)

# a = "abba"
# print(a[::-1])

# 234. Palindrome Linked List


# 13. Roman to Integer
class Solution(object):
    def romanToInt(self, s):
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0

        for i in range(len(s)):
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
# 1 stop one bofore loop 
# 2 subtract the small val
                total -= values[s[i]]
            else:  ## later add the value or simply add
                total += values[s[i]]

        return total
solution = Solution()
answer = solution.romanToInt("MCMXCIV")
print(answer)

# s = "MCMXCIV"
# print(list(s))
# print(s)
