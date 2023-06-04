"""
2258. Escape the Spreading Fire
"""


from collections import deque
from copy import deepcopy
from typing import List


class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        """
        Cleaned from Dicussion
        """
        FIRE = 1
        WALL = 2

        ROWS = len(grid)
        COLS = len(grid[0])

        SAFEHOUSE = (ROWS - 1, COLS - 1)

        fire_minutes = [[-1] * COLS for _ in range(ROWS)]
        person_minutes = [[-1] * COLS for _ in range(ROWS)]

        dy = [-1, 1, 0, 0]
        dx = [0, 0, -1, 1]

        def is_valid(y, x):
            if 0 <= y < ROWS and 0 <= x < COLS:
                return True
            return False

        def bfs(adjacents: deque, minutes, is_person) -> None:
            while adjacents:
                y, x, minute = adjacents.popleft()
                minutes[y][x] = minute

                for d in range(4):
                    ny = y + dy[d]
                    nx = x + dx[d]

                    if (
                        # if out of bounds
                        not is_valid(ny, nx)
                        # if there's a wall
                        or grid[ny][nx] == WALL
                        # if already moved here / if it's already in flames
                        or 0 <= minutes[ny][nx] <= minute + 1
                    ):
                        continue

                    if (
                        is_person
                        # if adjacent is safehouse
                        and (ny, nx) == SAFEHOUSE
                        # if fire gets at safehouse at the same time as person
                        and fire_minutes[ny][nx] == minute + 1
                    ):
                        adjacents.append((ny, nx, minute + 1))
                        continue

                    # if adjacent cell in person's path is in flames
                    if is_person and 0 <= fire_minutes[ny][nx] <= minute + 1:
                        # don't continue this path
                        continue

                    adjacents.append((ny, nx, minute + 1))

        # initial fires
        fires = deque([(r, c, 0) for r in range(ROWS) for c in range(COLS) if grid[r][c] == FIRE])
        # first check time that fire takes to spread
        bfs(fires, fire_minutes, False)

        person = deque([(0, 0, 0)])
        # then check time that person takes to safehouse
        bfs(person, person_minutes, True)

        # minutes that person took to reach safehouse
        person_to_safehouse = person_minutes[-1][-1]
        # minutes that fire took to reach safehouse
        fire_to_safehouse = fire_minutes[-1][-1]

        # if person could never reach safehouse
        if person_to_safehouse < 0:
            return -1
        # if fire could never reach safehouse
        if fire_to_safehouse < 0:
            return 10**9

        # difference in minutes for fire to reach safehouse after person
        diff_to_safehouse = fire_to_safehouse - person_to_safehouse

        if diff_to_safehouse == 0:
            return 0

        # left and above cells of safehouse are its only entries.
        # it's possible for both person and fire to reach the safehouse from diferent directions:

        # minutes that person took to reach:
        # left cell of safehouse
        person_to_left = person_minutes[-1][-2]
        # above cell of safehouse
        person_to_above = person_minutes[-2][-1]

        # minutes the fire took to reach:
        # left cell of safehouse
        fire_to_left = fire_minutes[-1][-2]
        # above cell of safehouse
        fire_to_above = fire_minutes[-2][-1]

        # difference in minutes for fire to reach left cell after person
        diff_to_left = fire_to_left - person_to_left
        # difference in minutes for fire to reach above cell after person
        diff_to_above = fire_to_above - person_to_above

        # if fire took longer to catch up person on left cell,
        # then entering from above is faster (or the other way around)
        if diff_to_left > diff_to_safehouse or diff_to_above > diff_to_safehouse:
            # so person can wait an extra minute because of the alternative path
            return diff_to_safehouse

        return diff_to_safehouse - 1


if __name__ == "__main__":
    solution = Solution()
    grids = [
        [[0, 2, 0, 0, 0, 0, 0], [0, 0, 0, 2, 2, 1, 0], [0, 2, 0, 0, 1, 2, 0], [0, 0, 2, 2, 2, 0, 2], [0, 0, 0, 0, 0, 0, 0]],
        [[0, 0, 0, 0], [0, 1, 2, 0], [0, 2, 0, 0]],
        [[0, 0, 0], [2, 2, 0], [1, 2, 0]],
    ]
    output = [3, -1, 1000000000]

    for g in grids:
        print("#", solution.maximumMinutes(g))
