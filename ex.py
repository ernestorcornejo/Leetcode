class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            midval = (high + low) // 2
            if nums[midval] == target:
                return midval
            elif nums[midval] < target:
                low = midval + 1
            else:
                high = midval - 1
        return -1