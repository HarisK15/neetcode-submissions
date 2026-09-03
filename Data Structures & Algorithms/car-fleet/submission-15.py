class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        #method: calcualte for each index (correspondant) what time they reach 10 miles
        stack = []
        pairs = [(p,s) for p,s in zip(position, speed)]
        pairs.sort(reverse=True)
        for p,s in pairs:
            diff = target - p
            tta = (diff/s)
            if stack and tta <= stack[-1]:
                continue
            else:
                stack.append(tta)

        return(len(stack))



        