class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def diameter(self):
        return self._radius * 2
    
class MathUtils:
    @staticmethod
    def is_even(n):
        return n % 2 == 0
        
class Product:
    TAX_RATE = 0.1 # 클래스 변수

    def __init__(self, price):
        self.price = price

    @classmethod
    def from_price_with_tax(cls, price_with_tax):
        """세금이 포함된 가격으로부터 객체를 생성합니다."""
        base_price = price_with_tax / (1 + cls.TAX_RATE)
        return cls(base_price) # cls는 Product 클래스를 가리킴, 즉 클라스를 생성하고 반환
    
"""
상속 관련 코드
"""
from abc import ABC, abstractmethod

class Shape(ABC): # ABC를 상속받아 추상 클래스로 지정
    @abstractmethod
    def area(self):
        """도형의 넓이를 계산합니다."""
        pass

    @abstractmethod
    def perimeter(self):
        """도형의 둘레를 계산합니다."""
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self): # 추상 메서드를 반드시 구현해야 함
        return self.width * self.height

    def perimeter(self): # 추상 메서드를 반드시 구현해야 함
        return 2 * (self.width + self.height)

if __name__ == "__main__":
    circle = Circle(5)
    print(f"반지름: {circle._radius}")
    #@property - 메서드를 클래스의 속성(attribute)처럼 호출할 수 있게 만듭니다. 값에 접근할 때 추가적인 로직(예: 계산, 유효성 검사)을 실행하고 싶을 때 유용합니다.
    print(f"지름: {circle.diameter}")
    #@staticmethod - 클래스나 인스턴스의 상태에 접근할 필요가 없는 유틸리티성 함수에 사용합니다. self나 cls를 첫 인자로 받지 않으며, 클래스 이름을 통해 직접 호출할 수 있습니다.
    print(MathUtils.is_even(10))
    #@classmethod - 인스턴스 대신 클래스 자체(cls)를 첫 인자로 받습니다. 클래스 변수를 사용하거나, 클래스 자체와 관련된 작업을 할 때 사용됩니다. 주로 팩토리 메서드(factory method)를 만드는 데 활용됩니다.
    p1 = Product(100)
    p2 = Product.from_price_with_tax(110)
    print(f"p1 가격: {p1.price:.2f}")
    print(f"p2 가격: {p2.price:.2f}")

    #상속 - abc (Abstract Base Classes) 모듈을 사용하여 만들며, 직접 인스턴스화할 수 없습니다. 이는 여러 하위 클래스가 공통된 인터페이스를 갖도록 강제하여 코드의 일관성을 높입니다.
    r = Rectangle(10, 5)
    print(f"사각형 넓이: {r.area()}")