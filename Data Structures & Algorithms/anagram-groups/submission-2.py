from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        list_char_count = [] # this list will store all the character frequency dictionaries
        for word in strs:
            char_count = dict(Counter(word)) # get a character frequency dictionary for a word
            if char_count not in list_char_count: # check to make sure there's no duplicate dictionaries
                list_char_count.append(char_count)

        group_maps = []
        for maps in list_char_count: # go through each unique freq dic
            group = []
            for word in strs:
                if dict(Counter(word)) == maps: # check if the maps are the same
                    group.append(word) # append to common maps list
            group_maps.append(group) # append sublist to main list
        
        return group_maps





        