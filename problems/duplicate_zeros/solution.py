class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        while 1:
            if i == len(arr) or i == len(arr) + 1:
                break
            if arr[i] == 0:
                arr.insert(i,0)
                arr.pop()
                i += 2
            else:
                i += 1