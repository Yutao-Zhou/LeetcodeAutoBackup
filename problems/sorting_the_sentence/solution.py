class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans=[]
        word = s.split()
        word = sorted(word, key = lambda x : x[-1])
        for i in range(len(word)):
            words = (word[i][:len(word[i])-1])
            ans.append(words)
        return ' '.join(ans)