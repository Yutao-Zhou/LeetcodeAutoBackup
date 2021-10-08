class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        ans = []
        com = list(command)
        i = 0
        while i < len(com):
            if com[i] == 'G':
                ans.append('G')
                i += 1
            elif com[i] == '(':
                if com[i+1] == ')':
                    ans.append("o")
                    i += 2
                else:
                    ans.append('al')
                    i += 4
        return ''.join(ans)
            
        