class MaximumSubsetBit:
    def __init__(self):
        pass

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or_val= 0
        for num in nums:
            max_or_val |= num
        return self.count_subsets(nums, 0, 0, max_or_val)

    def count_subsets(self, nums:List[int], index:int, current_or:int, target_or:int) -> int:
        # base case: reached the end of the array
        if(index == len(nums)):
            return 1 if current_or == target_or else 0

        # don't include the current number
        count_without= self.count_subsets(nums, index+1, current_or, target_or)
        # include the current number
        count_with = self.count_subsets(nums, index+1, current_or | nums[index], target_or)
        # return the sum of both cases
        return count_without + count_with
