class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     current = 0
    #     add1 = add2 = None

    #     while(current < len(nums)):
    #         for i in range(len(nums)):
    #             if i == current:
    #                 continue
    #             elif nums[current] + nums[i] == target:
    #                 add1 = min(current, i)
    #                 add2 = max(current, i)
    #         current += 1
        
    #     if add1 != None:
    #         return (add1, add2)
        
    #     return None
    # GPT optimal
    # Can you come up with an algorithm that is less than O(n2) time complexity?
        # each num processed once O(n), 
        # dict lookups are O(1) on average, 
        # we never reuse the same element because we only check prev seen values
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
    


                


        