# https://leetcode.com/problems/word-break/

import functools
from collections import deque

class Solution:
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        q = deque([0]) # deque of indices
        seen = set()
        
        while q:
            start = q.popleft()
            if start == len(s):
                return True
            
            for end in range(start+1, len(s)+1):
                if end in seen:
                    # 기처리
                    continue
                if s[start:end] in words:
                    q.append(end)
                    seen.add(end)
        return False
       
        