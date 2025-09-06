def greet():
    return "Hello from module1 (public)"

def _internal_helper():
    return "This is for internal use"

# greet 함수만 외부에 공개하도록 지정
__all__ = ['greet']