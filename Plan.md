# Plan

## 검증할 동작
모든 투구가 거터(0핀)일 때 게임 총점은 0이어야 한다. (가장 단순한 케이스로 `Game` 클래스의 기본 골격을 세운다.)

## 작성할 테스트
`test_game.py`에 다음 테스트를 추가한다.

```python
from game import Game


def test_all_gutter_balls_scores_zero():
    game = Game()

    for _ in range(20):
        game.roll(0)

    assert game.score() == 0
```

## 구현 계획 (테스트를 통과시키기 위한 프로덕션 코드)
`game.py`에 `Game` 클래스를 새로 만든다.

- `__init__`: 투구 기록을 저장할 `self._rolls = []`를 초기화한다.
- `roll(pins)`: 아직 아무 동작도 하지 않는다 (이번 테스트는 `roll` 자체의 부수효과를 검증하지 않음).
- `score()`: `0`을 하드코딩하여 반환한다.

## 범위 제한 (이번 사이클에서 하지 않는 것)
- 투구 합산, 스페어/스트라이크 보너스, 10번 프레임 규칙은 다루지 않는다 — 각각 이후 별도의 PLAN-RED-GREEN-REVIEW 사이클에서 추가한다.
