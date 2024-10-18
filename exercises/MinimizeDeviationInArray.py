
"""
1675. Minimize Deviation in Array
https://leetcode.com/problems/minimize-deviation-in-array/description/
You are given an array nums of n positive integers.

You can perform two types of operations on any element of the array any number of times:

If the element is even, divide it by 2.
For example, if the array is [1,2,3,4], then you can do this operation on the last element, and the array will be [1,2,3,2].
If the element is odd, multiply it by 2.
For example, if the array is [1,2,3,4], then you can do this operation on the first element, and the array will be [2,2,3,4].
The deviation of the array is the maximum difference between any two elements in the array.

Return the minimum deviation the array can have after performing some number of operations.

"""

class MinimizeDeviationInArray:

    def minimumDeviation(self, nums: List[int]) -> int:
        minHeap, heapMax = [], 0
        for n in nums:
            tmp = n
            while n% 2 == 0:
                n = n // 2
            minHeap.append((n,  max(tmp, 2 * n)))
            heapMax = max(heapMax, n)

        res = float("inf")
        heapq.heapify(minHeap)
        while len(minHeap) == len(nums):
            n, nMax = heapq.heappop(minHeap)
            res = min(res, heapMax - n)

            if n < nMax:
                heapq.heappush(minHeap, (n*2, nMax))
                heapMax = max(heapMax, n * 2)

        return res
