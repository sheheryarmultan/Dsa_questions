class Solution(object):
    def pivotIndex(self, nums):

        suml=0

        total=sum(nums)
        for i in range(0,len(nums)):
            sumr=total-suml-nums[i]
            if sumr==suml:
                return i
            suml=suml+nums[i]
        return -1




nums = [1, 7, 3, 6, 5, 6]
solution=Solution()
result=solution.pivotIndex(nums)
print(result)
