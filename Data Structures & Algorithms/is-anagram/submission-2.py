class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): # if lengths are not the same then it's obviously false
            return False

        def char_counter(word): # helper function to count characters in word (there's a function for this)
            word_dict = {}
            for char in word:
                if char in word_dict:
                    word_dict[char] += 1
                else:
                    word_dict[char] = 1
            return word_dict
        
        s_dict = char_counter(s)
        t_dict = char_counter(t)

        for char in s_dict: # compare the count of each character in the word
            if char in t_dict:
                if s_dict[char] != t_dict[char]:
                    return False
            else:
                return False
        return True
            

        