class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        first=strs[0]

        for i in range(len(first)):
            char=first[i]
            for j in strs:
                if i>=len(j) or j[i] != char:
                    return first[:i]
        return first 
        