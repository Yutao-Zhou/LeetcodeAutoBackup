class Solution:
    str2index = {"type":0,"color":1,"name":2}
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ans = 0
        for item in items:
            if item[self.str2index[ruleKey]] == ruleValue:
                ans += 1
        return ans