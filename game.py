class Game:
    def __init__(self):
        self._rolls = []

    def roll(self, pins):
        self._rolls.append(pins)

    def score(self):
        total = 0
        i = 0
        for _ in range(9):
            if self._is_strike(i):
                frame_score = 10 + self._rolls[i + 1] + self._rolls[i + 2]
                i += 1
            else:
                frame_score = self._rolls[i] + self._rolls[i + 1]
                if self._is_spare(frame_score):
                    frame_score += self._rolls[i + 2]
                i += 2
            total += frame_score
        total += sum(self._rolls[i:])
        return total

    def _is_strike(self, i):
        return self._rolls[i] == 10

    def _is_spare(self, frame_score):
        return frame_score == 10
