from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        mylist = []
        otherList = []
        someval = 0

        #[4,1,0,3,10]
        #[100,16,9,1]

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                someval = nums[left] * nums[left]
                mylist.append(someval)
                left += 1
            else:
                #abs(nums[left]) < abs(nums[right])
                someval = nums[right] * nums[right]
                mylist.append(someval)
                right -= 1

        # otherList = Solution.reverseMe(mylist)
        # return otherList

    # def reverseMe(nums: List[int]) -> List[int]:
    #     left = 0
    #     right = len(nums) - 1
    #     mylist = []

    #     while left <= right:
    #         if nums[left] > nums[right]:
    #             mylist.append(nums[right])
    #             right -= 1
    #         else:
    #             mylist.append(nums[left])
    #             left += 1
        mylist.reverse()
        return mylist