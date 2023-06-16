# https://leetcode.com/problems/largest-divisible-subset/
from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        ## 새로운 num이 있을 때 이전 num 중 가장 큰 num
        d = dict() # {해당 수: 해당 수의 공약수들}
        nums.sort()
        for num in nums:
            d[num] = []
            if num == 1:
                d[num] = [1]
                continue
            for key in d.keys():
                if key != num and num % key == 0:
                    if len(d[key]) > len(d[num]):
                        d[num] = d[key].copy() # d[key] 하면 동기화됨
                        
            d[num].append(num)


        ls = sorted(d.values(), key = len)
        return ls[-1]