class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        a = operations.count("++X")
        b = operations.count("X++")
        c = operations.count("--X")
        d = operations.count("X--")
        ans = a+b-c-d
        return ans
        
        