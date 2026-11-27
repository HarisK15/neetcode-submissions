class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sort_num = sorted(nums)
        n = len(sort_num)
        p3 = n - 1
        p1, p2 = 0, p3 - 1

        sols = []


        while p3 >= 2:
            num1, num2, num3 = sort_num[p1], sort_num[p2], sort_num[p3]
            if num1 + num2 == -num3:
                if [num1, num2, num3] not in sols:
                    sols.append([num1, num2, num3])
                p1 += 1

            if num1 + num2 > -num3:
                p2 -= 1

            elif num1 + num2 < -num3:
                p1 += 1
            # if p1 >= p2:

            if p1 == p2:
                p3 -= 1
                p1 = 0
                p2 = p3 - 1
        return sols
        # return(sols)