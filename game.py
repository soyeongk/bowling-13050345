class Game:
    def __init__(self):
        self._rolls = []

    def roll(self, pins):
        self._rolls.append(pins)

    def score(self):
        total = 0
        i = 0
        for _ in range(10):
            frame_score = self._rolls[i] + self._rolls[i + 1]
            if frame_score == 10:
                frame_score += self._rolls[i + 2]
            total += frame_score
            i += 2
        return total
