class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        freq_map = {}
        for word in strs:
            char_count = tuple(sorted(dict(Counter(word)).items()))
            if char_count in freq_map:
                freq_map[char_count].append(word)
            else:
                freq_map[char_count] = [word]

        freq_map_list = []

        for x in freq_map:
            freq_map_list.append(freq_map[x])

        return freq_map_list            

        