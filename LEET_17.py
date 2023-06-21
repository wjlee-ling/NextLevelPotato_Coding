"""
17. Letter Combinations of a Phone Number
"""
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {}
        idx = 97
        for num in range(2, 10):
            num = str(num)
            if num == "7" or num == "9":
                for _ in range(4):
                    letters.setdefault(num, "")
                    letters[num] += chr(idx)
                    idx += 1
            else:
                for _ in range(3):
                    letters.setdefault(num, "")
                    letters[num] += chr(idx)
                    idx += 1
        # print(letters)

        if digits:
            answer = [""]
        else:
            return []

        for digit in digits:
            combinations = []
            for letter in letters[digit]:
                for combination in answer:
                    combinations.append(combination + letter)
                    # print(answer)

            answer = combinations

        return answer


if __name__ == "__main__":
    solution = Solution()
    digits = ["23", "", "2", "234"]
    output = [
        ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"],
        ["a", "b", "c"],
        [
            "adg",
            "bdg",
            "cdg",
            "aeg",
            "beg",
            "ceg",
            "afg",
            "bfg",
            "cfg",
            "adh",
            "bdh",
            "cdh",
            "aeh",
            "beh",
            "ceh",
            "afh",
            "bfh",
            "cfh",
            "adi",
            "bdi",
            "cdi",
            "aei",
            "bei",
            "cei",
            "afi",
            "bfi",
            "cfi",
        ],
    ]

    for d in digits:
        print(solution.letterCombinations(d))
