# Plan

## 검증할 동작
스트라이크/스페어가 전혀 없을 때, 총점은 모든 투구 핀 수의 단순 합이어야 한다. (모든 투구가 1핀인 20회 게임 → 20점)

## 작성할 테스트
`test_game.py`에 다음 테스트를 추가한다.

```python
def test_all_ones_scores_twenty():
    game = Game()

    for _ in range(20):
        game.roll(1)

    assert game.score() == 20
```

## 구현 계획 (테스트를 통과시키기 위한 프로덕션 코드)
`game.py`를 다음과 같이 수정한다.

- `roll(pins)`: `self._rolls.append(pins)`로 투구를 기록한다.
- `score()`: `sum(self._rolls)`를 반환한다 (하드코딩된 0 제거).

## 범위 제한 (이번 사이클에서 하지 않는 것)
- 스페어/스트라이크 보너스, 10번 프레임 규칙은 다루지 않는다.
