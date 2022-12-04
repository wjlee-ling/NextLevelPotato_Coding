"""
solved
"""


def solution(s):
    answer = ""
    for word in s.split(" "):
        if word:
            answer += word[0].upper() + word[1:].lower() + " "
        else:
            answer += " "

    return answer[:-1]


if __name__ == "__main__":
    s = ["3people unFollowed me", "for the last week", "        FFFF FF       FFAAA      AAAb bbbbbb bbbb           "]
    results = ["3people Unfollowed Me", "For The Last Week"]
    for inputs in s:
        print(solution(inputs))
