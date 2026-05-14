class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        def char_counter(word):
            word_dict = {}
            for char in word:
                if char in word_dict:
                    word_dict[char] += 1
                else:
                    word_dict[char] = 1
            return word_dict
        
        s_dict = char_counter(s)
        t_dict = char_counter(t)

        for char in s_dict:
            if char in t_dict:
                if s_dict[char] != t_dict[char]:
                    return False
            else:
                return False
        return True
            

        