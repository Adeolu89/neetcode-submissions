from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        char_maps = []
        for word in strs:
            count = dict(Counter(word))
            if count not in char_maps:
                char_maps.append(count)

        group_maps = []
        for maps in char_maps:
            group = []
            for word in strs:
                if dict(Counter(word)) == maps:
                    group.append(word)
            group_maps.append(group)
        
        return group_maps





        