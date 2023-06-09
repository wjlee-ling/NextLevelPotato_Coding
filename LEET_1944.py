class Solution:
    def canSeePersonsCount(self, heights):
        answer = [0] * len(heights)
        stack = []
        for i, height in enumerate(heights):
            while stack and heights[stack[-1]] <= height:
                # 새로운 height보다 키작은 이전 애들은 더이상 볼 수 없음
                answer[stack.pop()] += 1
            if stack:
                # 새로운 애들보다 키가 큰 첫번째 애도 볼 수 있음
                answer[stack[-1]] += 1
            stack.append(i)