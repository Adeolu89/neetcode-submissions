class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}

        for x in range(len(nums)):
            new_target = target - nums[x]
            if new_target in hashmap:
                return sorted([hashmap[new_target], x])
            else:
                hashmap[nums[x]] = x
        

        



        