class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or s == None:
            return 0
        
        left_i = 0
        right_i = left_i + 1
        longest_string = s[left_i]
        string = longest_string
        
        while right_i < len(s):
            if s[right_i] in string:
                left_i += 1
                string = s[left_i:right_i]
            else:
                string += s[right_i]
                if len(longest_string) < len(string):
                    longest_string = string
                right_i += 1
                
        return len(longest_string)