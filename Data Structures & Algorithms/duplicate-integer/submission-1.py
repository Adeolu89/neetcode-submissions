class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_dict = {}
        for x in nums:
            if x in nums_dict:
                nums_dict[x] += 1
            else:
                nums_dict[x] = 1
        
        for x in nums_dict:
            count = nums_dict[x]
            if count > 1:
                return True
        return False
        