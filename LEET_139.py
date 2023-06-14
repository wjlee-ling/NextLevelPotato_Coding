"""
139. Word Break
"""


from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        length = len(s)
        dp = [False for i in range(length + 1)]
        dp[0] = True

        for i in range(1, length + 1):
            for word in wordDict:
                if s[i - len(word) : i] == word and dp[i - len(word)]:
                    dp[i] = True
                print(dp)

        return dp[-1]


if __name__ == "__main__":
    solution = Solution()
    strings = ["leetcode", "applepenapple", "catsandog"]
    wordDicts = [["leet", "code"], ["apple", "pen"], ["cats", "dog", "sand", "and", "cat"]]
    output = ["true", "true", "false"]

    for s, w in zip(strings, wordDicts):
        print(solution.wordBreak(s, w))

# 1. s를 분리, 조합하여 wordDict의 단어가 되는지 확인한다?
# 2. wordDict를 조합하여 s가 되는지 확인한다?
