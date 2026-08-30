class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        counts = [0,0,0]


        for i in nums:
            counts[i] +=1

        s = 0
        for i,n in enumerate(counts):
            j = n
            while j > 0:
                nums[s] = i
                j -= 1
                s += 1

        print(nums)




