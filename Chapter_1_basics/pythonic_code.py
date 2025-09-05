#아름다운 것이 추한 것보다 낫다 (Beautiful is better than ugly)

def dirty_swap(): #1. 숫자 교체 예시 - 더러운 버전
    a = 5
    b = 10
    temp = a
    a = b
    b = temp
    print(a, b)

def clean_swap(): #1. 숫자 교체 예시 - 클린 버전
    a, b = 5, 10
    a, b = b, a
    print(a, b)

def string_docs_test(a, b): #3. doc string
    """
      String docs 테스트
    """
    return a + b


def list_comprehension(): #4. list comprehension
    #더러운 예시
    squares = []
    for i in range(1, 6):
        squares.append(i**2)
    print(squares)

    #깔끔 예시
    squares_comprehension = [i**2 for i in range(1, 6)]
    print(squares_comprehension)

def lambda_test(): #5. lambda
    #더하기 함수를 람다로 표현
    add = lambda a, b : a + b
    print(add(3, 5))

    #리스트 정렬에 람다 사용
    points = [(1, 2), (-1, 5), (3, -4)]
    # 각 튜플의 두 번째 요소를 기준으로 정렬
    points.sort(key=lambda p: p[1])
    print(points)

def generator(): #6.Generator
    def count_up_to(max_num):
        count = 1
        while count <= max_num:
            yield count #제너레이터 방식의 return - 사용되면 다시 사용 불가
            count += 1

    #제너레이터 생성
    counter = count_up_to(5) #여기서 메모리에 1,2,3,4,5가 모두 저장되지 않고 loop을 돌릴때마다 각자 값을 반환

    print(next(counter))
    print(next(counter))

    for num in counter:
        print(num, end=' ')

def exceiption_example(): #7. Exception
    try:
        num = int(input("숫자를 입력하세요: "))
        result = 10 / num
    except ValueError:
        print("잘못된 입력입니다. 숫자를 입력해주세요.")
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다.")
    else:
        # 예외가 발생하지 않았을 때 실행
        print(f"결과는 {result}입니다.")
    finally:
        # 항상 실행
        print("프로그램을 종료합니다.")

#7. 사용자 정의 예외
class CustomExeption(Exception):
    """사용자 정의 예외 클라스"""
    pass

def exception_example_second(): #7. Exception
    def check_positive(number):
        if number <= 0:
            raise CustomExeption("숫자는 0보다 커야 합니다")
        print(f"{number}은(는) 양수입니다.")
    
    try:
        check_positive(-5)
    except CustomExeption as e:
        print(f"오류 발생: {e}")

if __name__ == "__main__":
    """
    1. 숫자 교체 예시
    """
    print("----Swap----")
    dirty_swap()
    clean_swap()
    print()

    """
    2. 네이밍, 변수, 함수, 클라스 이름 규칙과 관례
     변수와 함수 - 모든 글자를 소문자로 쓰고 단어 사이는 밑줄로 연결 (Snake-case) : user_name, calculate_total_price
     클라수 - 각 단어의 첫 글자는 대분자로 쓰고 단어 사이는 그대로 붙여쓰기 : UserAccount, HttpRequest
     상수 - 모든 글자를 대문자로 쓰고, 단어 사이는 밑줄로 연결 : MAX_CONNECTIONS, DEFAULT_TIMEOUT
    """

    """
    3. Docstrings
     설명 문자열  - 지금 해당 내용에 사용하는 주석이다 또한 내장 함수 help()나 __doc__속성을 통해 언제든지 내용 확인이 가능하다
    """
    print("----Doc strings----")
    print(string_docs_test.__doc__) #주석 출력
    help(string_docs_test) #함수, 매개변수, 주석 출력
    print()

    """
    4. List Comprehension
    """
    print("----List Comprehension----")
    list_comprehension()
    print()

    """
    5. Lambda
    주로 map(), filter(), sorted()와 같이 함수를 인자로 받는 함수와 함께 사용될 때 유용
    """
    print("----Lambda----")
    lambda_test()
    print()


    """
    6. Generator
    메모리에 효율적인 iterator 생성 - Java의 Stream과 유사
    함수 안에서는 return 대신 yield 키워드를 사용하면 제너레이터가 된다.
    """
    print("----Generator----")
    generator()
    print()

    """
    7. 예외처리(Exception Handling): try, except, finally를 이용한 오류 관리
    """
    print("----Generator----")
    exceiption_example()
    exception_example_second()
    print()