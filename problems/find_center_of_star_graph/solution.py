class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        set1 = set(edges[0])
        ans = set1.intersection(edges[1])
        return list(ans)[0]