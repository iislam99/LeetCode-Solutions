class Solution(object):    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0 or s == None:
            return ""
        
        longest_p = ""
        length = 0
        
        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > length:
                    longest_p = s[left : right + 1]
                    length = right - left + 1
                left -= 1
                right += 1
                
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > length:
                    longest_p = s[left : right + 1]
                    length = right - left + 1
                left -= 1
                right += 1
         
        return longest_p