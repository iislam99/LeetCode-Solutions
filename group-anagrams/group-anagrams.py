class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        match = {}
        
        for word in strs:
            sort = ''.join(sorted(word))
            if sort not in match:
                match[sort] = []
            match[sort].append(word)

        return match.values()