class Solution(object):
    def removeElement(self, nums, val):
        k=len(nums)
        for i in range(len(nums) - 1, -1, -1):

            if nums[i] == val:
                nums.remove(val)
                k=k-1
        return k


solution = Solution()
nums = [0, 1, 2, 2, 3, 0, 4, 2]
result = solution.removeElement(nums, 2)
print(nums)
