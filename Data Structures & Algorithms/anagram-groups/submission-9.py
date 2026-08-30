from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        prev = defaultdict(list)

        for i in strs:
            pos = 26*[0]
            for j in i:
                pos[ord(j) - ord("a")]+=1
            prev[tuple(pos)].append(i)


        return list(prev.values())


       