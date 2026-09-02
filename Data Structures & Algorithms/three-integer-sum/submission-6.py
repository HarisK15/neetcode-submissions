class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)-1):
            L = i+1
            R = len(nums)-1


            if i>0 and nums[i] == nums[i-1]:
                continue


            while L<R:


                if nums[L] + nums[R] + nums[i] > 0:
                    R-=1

                elif nums[L] + nums[R] + nums[i] < 0:
                    L+=1

                else:
                    res.append([nums[L],nums[R],nums[i]])
                    L+=1
                    R-=1
                    while nums[L]==nums[L-1] and L<R:
                        L+=1



        return res
                    
        
