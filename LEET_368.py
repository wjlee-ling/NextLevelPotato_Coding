# https://leetcode.com/problems/largest-divisible-subset/

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        ## 새로운 num이 있을 때 이전 num 중 가장 공약수가 많은 숫자 선택
        d = dict() # {가장 작은 수: 배수}
        nums.sort()
        for num in nums:
            flag = 0
            for k in d.keys():
                if num % k == 0 and k != 1:
                    d[k].append(num)
                    flag = 1
                elif k % num == 0:
                    d[num].append(k)
                    flag = 1
            if flag == 0:
                ## 기존에 있는 것과 안됨
                d[num] = [num]
                if nums[0] == 1 and num !=1:
                    d[num].append(1)
        print(d)
        ls = sorted(d.values(), key = len)
        return ls[-1]