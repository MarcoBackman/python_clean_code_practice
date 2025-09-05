from collections import namedtuple, defaultdict
import sys

def set_example(): #중복을 허용하지 않는 유일한 요소들의 순서 없는 모음
    my_list = [1, 2, 2, 3, 4, 4, 4]
    unique_items = set(my_list)
    print(unique_items)  # 출력: {1, 2, 3, 4}

    # 멤버십 테스트 (리스트보다 훨씬 빠름)
    if 3 in unique_items:
        print("3이 존재합니다.")

def named_tuple(): #named tuple
    # 'Point'라는 이름의 네임드 튜플 정의
    Point = namedtuple('Point', ['x', 'y'])
    p1 = Point(10, 20)

    print(p1.x, p1.y)     # 이름으로 접근 (출력: 10 20)
    print(p1[0], p1[1])   # 인덱스로 접근 (출력: 10 20)


def str_bytes_example():
    # str (유니코드 문자열)
    text = "안녕하세요"

    # str -> bytes (인코딩)
    encoded_text = text.encode('utf-8')
    print(encoded_text)  # 출력: b'\xec\x95\x88\xeb\x85\x95\xed\x95\x98\xec\x84\xb8\xec\x9a\x94'

    # bytes -> str (디코딩)
    decoded_text = encoded_text.decode('utf-8')
    print(decoded_text)  # 출력: 안녕하세요

def list_and_generator():
    # 리스트: 100만 개의 숫자를 메모리에 모두 저장
    list_data = [i for i in range(1000000)]
    print(f"리스트 메모리 사용량: {sys.getsizeof(list_data)} 바이트")

    # 제너레이터: 객체 자체의 크기만 차지
    gen_data = (i for i in range(1000000))
    print(f"제너레이터 메모리 사용량: {sys.getsizeof(gen_data)} 바이트")


def extra_features():
    #Dictionary
    """
    def handle_command(command):
        # command에 해당하는 함수를 찾아 실행, 없으면 기본 함수 실행
        return {
            'start': start_function,
            'stop': stop_function,
            'pause': pause_function,
        }.get(command, default_function)
    """
    
    #Dictionary merge
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    merged = dict1 | dict2
    print(merged) # 출력: {'a': 1, 'b': 3, 'c': 4} (중복된 키는 오른쪽 값으로 갱신됨)


    #Default dictionary
    text = "hello world"
    # 존재하지 않는 키를 조회하면 기본값으로 정수 0을 반환
    char_count = defaultdict(int)
    for char in text:
        char_count[char] += 1 # 키 존재 여부 확인 불필요

    print(char_count)
    # 출력: defaultdict(<class 'int'>, {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

# handle_command('start')()  # start_function 실행

    pass

if __name__ == "__main__":
    """
    1. Set
    합집합 (|), 교집합(&), 차집합(-) 등 수학적인 집합 연산 지원
    """
    print("----Swap----")
    set_example()
    print()

    """
    2. Named tuple - collections.namedtuple
    각 요소에 이름을 부여하여 접근할 수 있게 만든 튜플입니다.
    일반 튜플처럼 인덱스로도 접근할 수 있지만, 점(.)을 이용해 이름으로 접근하면 코드의 가독성이 크게 향상
    """
    print("----Named tuple----")
    named_tuple()
    print()

    """
    3. str, bytes
     str: 사람을 위한 텍스트 데이터를 다룹니다. 유니코드 문자의 시퀀스로, 파일이나 네트워크로 전송하려면 특정 인코딩(예: UTF-8)을 통해 bytes로 변환(encode())해야 합니다.
     bytes: 기계를 위한 이진 데이터를 다룹니다. 0부터 255까지의 정수 시퀀스로, 이미지, 동영상 파일 또는 네트워크 패킷과 같은 데이터를 표현합니다. bytes를 사람이 읽을 수 있는 텍스트로 바꾸려면 디코딩(decode())해야 합니다.
    """
    print("----str and bytes with encoding and decoding----")
    str_bytes_example()
    print()

    """
    4. List and Generator
     리스트: 모든 데이터를 메모리에 미리 로드합니다. 따라서 데이터의 크기가 크면 메모리 사용량이 급증할 수 있습니다. 하지만 모든 데이터가 이미 메모리에 있으므로 인덱싱이나 슬라이싱 등 무작위 접근이 빠릅니다.
     제너레이터: 데이터를 필요할 때마다 하나씩 생성합니다. yield 키워드를 통해 값을 반환하며, 현재 상태를 기억했다가 다음 요청 시 이어서 값을 생성합니다. 따라서 대용량 데이터를 처리할 때 메모리를 매우 효율적으로 사용할 수 있습니다.
    """
    print("----List and Generator----")
    list_and_generator()
    print()

    """
    5. 그 외 기본 기능들
        zip, dict, switch, dictionary merge(above 3.9), defaultdict
    """
    print("----Extra features----")
    extra_features()
    print()
