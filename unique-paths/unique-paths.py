class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        sol = 1
        num_moves = n + m - 2
        choose = min(n, m)
        
        i = 1
        while i < choose:
            sol = sol * num_moves / i
            i += 1
            num_moves -= 1
        
        return sol