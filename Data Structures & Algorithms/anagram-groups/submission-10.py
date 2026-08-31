from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)


        for word in strs:
            pos = [0]*26
            for char in word:
                pos[ord(char)-ord("a")] += 1

            res[tuple(pos)].append(word)

        return list(res.values())

        
