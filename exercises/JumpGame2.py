
class Solution:

    def jump(self,  nums: List[int]) --> int:
        #The starting range of the first jump is [0, 0]
        answer, n = 0, len(nums)
        curEnd, curFar = 0, 0

        for i in range(n -1):
            # update the farthest reacheble index of this jump,
            curFar = max(curFar, i + nums[i])

            ##If we finish the starting range of this jump,
            # Move on to the starting range of the next jump.
            if i == curEnd:
                answer += 1
                curEnd = curFar
        return answer
