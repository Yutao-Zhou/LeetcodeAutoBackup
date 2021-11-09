class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1 = 0
        n2 = 0
        for i in range(-1,-len(num1)-1,-1):
            n1 += int(num1[i])*10**abs(i+1)
        for i in range(-1,-len(num2)-1,-1):
            n2 += int(num2[i])*10**abs(i+1)
        return str(n1 + n2)
        