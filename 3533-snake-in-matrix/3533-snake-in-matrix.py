class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        row, col = 0, 0
        direction_map = {
            "UP": (-1, 0),
            "DOWN": (1, 0),
            "LEFT": (0, -1),
            "RIGHT": (0, 1)
        }
        for i in commands:
            dr, dc = direction_map[i]
            row += dr
            col += dc
        final_position = row * n + col
        return final_position