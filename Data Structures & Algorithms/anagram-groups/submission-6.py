from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ascii_map = defaultdict(list)
        for string in strs:
            newarr = 26*[0]
            for character in string:
                pos = ord(character) - ord("a")
                newarr[pos]+=1
            ascii_map[tuple(newarr)].append(string)


        return list(ascii_map.values())


       