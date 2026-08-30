###  4 pillars of oop 1 encapculation 2 inheritance 3 polymorphism 4 abstraction
### methodoverload , overrride

# 9. Palindrome Number
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

