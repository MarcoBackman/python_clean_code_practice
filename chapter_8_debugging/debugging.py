
def breakpoint_example():
    # 파일명: debug_example.py
    def calculate_sum(n):
        total = 0
        for i in range(n + 1):
            total += i
            if i == 5:
                # i가 5일 때 실행을 멈추고 디버거를 시작합니다.
                breakpoint() 
        return total
    print(calculate_sum(10))


def logging_example():
    # 파일명: logging_example.py
    import logging

    # 기본 로깅 설정 (DEBUG 레벨 이상의 로그를 모두 출력)
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    def factorial(n):
        logging.debug(f'factorial({n}) 호출됨')
        if n == 0:
            return 1
        else:
            result = n * factorial(n-1)
            logging.debug(f'factorial({n})의 결과: {result}')
            return result

    print(f"최종 결과: {factorial(3)}")


db = {}

def save_user(username):
    if len(username) < 3:
        raise ValueError("사용자명은 3글자 이상이어야 합니다.")
    db[username] = {"active": True}
    return True

# Pytest를 이용한 통합 테스트
def test_user_registration_flow():
    # 1. save_user 함수를 호출하여 사용자를 등록
    username = "testuser"
    result = save_user(username)

    # 2. 결과 및 DB 상태를 함께 검증
    assert result is True
    assert username in db
    assert db[username]["active"] is True




if __name__ == "__main__":
    #1. Breakpoint 를 이용한 오류 추적
    breakpoint_example()

    #2. logging 모듈을 이용한 분석 -  로그는 심각도(DEBUG, INFO, WARNING, ERROR 등)에 따라 등급부여
    logging_example()

    #3. Test framework - 터미널에서 pytest 명령어를 실행하면 test_math.py 파일을 찾아 test_add 함수를 자동으로 실행하고 결과를 알려줍니다. - test_math.py 참고할 것

    #4. Integration Test - 여러 개의 모듈(단위)을 결합했을 때, 이들이 서로 상호작용하며 예상대로 동작하는지 검증하는 테스트입니다
    test_user_registration_flow()

