from . import add

#유닛 테스트 용
def add(a, b):
    return a + b

# add 함수를 테스트하는 코드
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2