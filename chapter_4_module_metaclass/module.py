

if __name__ == "__main__":
    """
    1. 모듈과 패키지
    __init__.py 파일을 이용한 코드 구조화 - 파이썬에서 코드를 구조화하는 기본 단위는 모듈(module)과 패키지(package)입니다.
      모듈: 하나의 .py 파일. 함수, 클래스, 변수 등을 담을 수 있습니다.
      패키지: 모듈들을 모아놓은 디렉터리. 패키지로 인식되려면 내부에 __init__.py 파일이 있어야 합니다. (Python 3.3+ 부터는 필수는 아니지만, 호환성과 명시성을 위해 사용하는 것을 권장합니다.)

      ex) 
        my_package/
        ├── __init__.py
        ├── module1.py
        └── sub_package/
            ├── __init__.py
            └── module2.py
    """


    """
    2. 임포트(Import): 모듈/패키지 로딩 방법 및 __all__의 사용

        import 문은 다른 모듈의 코드를 현재 스코프로 가져오는 역할을 합니다.
        절대 임포트 (Absolute Import): 프로젝트의 최상위 디렉터리부터 전체 경로를 명시합니다. (from my_package.sub_package import module2) 가장 명확하고 권장되는 방식입니다.
        상대 임포트 (Relative Import): 현재 파일의 위치를 기준으로 임포트합니다. (from . import module1) 패키지 내부에서 다른 모듈을 참조할 때 유용합니다.

        __all__의 사용
        __all__은 from <module> import * 구문을 사용할 때, 외부에 공개할 이름(변수, 함수, 클래스)들의 리스트를 명시적으로 지정하는 역할을 합니다.
          이를 통해 모듈의 공개 API를 명확히 하고, 불필요한 이름이 외부에 노출되는 것을 방지할 수 있습니다.
    """
    from my_package.module1 import *

    print(greet()) # 정상적으로 임포트됨
    # print(_internal_helper()) # NameError 발생! __all__에 포함되지 않았기 때문

    """
    3. 메타클래스(Metaclass): 클래스를 만드는 클래스 - 클라스는 메타클래스가 만듭니다.
    type이 파이썬의 기본 메타클래스이며, 우리가 class 키워드로 클래스를 정의할 때 내부적으로 type이 호출되어 클래스 객체를 생성합니다.
    Django ORM이나 SQLAlchemy 같은 라이브러리에서 모델 클래스를 정의할 때 필드를 자동으로 등록하는 등 내부적으로 널리 사용
    """

    class EnforceModelSuffixMeta(type):
        # __new__는 클래스 객체 자체를 생성하는 메서드
        def __new__(cls, name, bases, dct):
            if not name.endswith("Model"):
                raise TypeError("클래스 이름은 'Model'로 끝나야 합니다.")
            return super().__new__(cls, name, bases, dct)

    # 메타클래스 적용
    class ProductModel(metaclass=EnforceModelSuffixMeta):
        pass

    """
    4. 특수 클라스 __new__
    __new__는 인스턴스를 생성하고 할당하는 역할을 하는 특수 메서드입니다. 
    __init__이 생성된 인스턴스를 초기화하는 반면, __new__는 인스턴스 생성 자체에 관여합니다.
    """

    class BaseShape:
        def __new__(cls, *args, **kwargs):
            # BaseShape 자체는 인스턴스화 가능
            if cls is BaseShape:
                return super().__new__(cls)
            # 서브클래스가 'area' 메서드를 구현했는지 검사
            if not hasattr(cls, 'area'):
                raise NotImplementedError(f"'{cls.__name__}' 클래스는 'area' 메서드를 구현해야 합니다.")
            return super().__new__(cls)

        def __init__(self):
            print(f"{self.__class__.__name__} 인스턴스 생성")

    class Rectangle(BaseShape):
        def area(self): # 'area' 구현
            return 10

    class Triangle(BaseShape):
        # 'area'를 구현하지 않음
        pass

    r = Rectangle() # 정상 동작
    # t = Triangle() # NotImplementedError 발생!

    """
    5. 특수 클라스 __slots__
    기본적으로 파이썬 클래스의 인스턴스는 __dict__라는 딕셔너리에 속성을 저장합니다. 이는 동적으로 속성을 추가/삭제할 수 있게 해주지만, 메모리를 많이 차지합니다.
    __slots__에 속성 이름들을 튜플이나 리스트로 지정하면, 파이썬은 __dict__를 생성하는 대신 더 적은 메모리를 사용하는 고정된 크기의 배열에 속성을 저장합니다.
      이는 수천, 수만 개의 인스턴스를 생성할 때 상당한 메모리 절약 효과를 가져옵니다.

      주의 할 점은 __slot__ 사용 시, 명시된 속성 외에 새로운 속성을 동적으로 추가가 불가하다
    """
    class Point:
        # __dict__를 사용하지 않고, x와 y를 위한 공간만 할당
        __slots__ = ('x', 'y')
        def __init__(self, x, y):
            self.x = x
            self.y = y

    p = Point(1, 2)
    print(p.x, p.y)


    """
    Descriptor: 속성 접근 제어
    디스크립터는 __get__, __set__, __delete__ 같은 특수 메서드를 구현한 객체로, 다른 객체의 속성(attribute)에 대한 접근을 제어하는 강력한 메커니즘입니다.
    속성에 접근할 때(get, set, delete) 미리 정의된 로직을 실행시킬 수 있습니다.

    @property, @staticmethod, @classmethod 데코레이터들이 바로 디스크립터 프로토콜을 활용하여 구현된 기능들입니다.
    """
    class Integer:
        def __init__(self):
            self._values = {}

        def __get__(self, instance, owner):
            # instance: 디스크립터를 소유한 객체 (e.g., p)
            # owner: 소유한 객체의 클래스 (e.g., Point)
            return self._values.get(instance)

        def __set__(self, instance, value):
            if not isinstance(value, int):
                raise TypeError("정수 값만 할당할 수 있습니다.")
            self._values[instance] = value

    class Point:
        x = Integer() # 디스크립터 인스턴스를 클래스 속성으로 할당
        y = Integer()

    p = Point()
    p.x = 10  # Integer.__set__ 호출
    p.y = 20
    print(p.x) # Integer.__get__ 호출

    # p.x = "hello" # TypeError 발생!