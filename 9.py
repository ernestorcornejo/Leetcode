class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x) #-121 abs --> 121
        reversed_s = s[::-1] # 121
        if s != reversed_s:
            return False
        else:
            return True
A = Solution()
something = A.isPalindrome(121)
print(something)