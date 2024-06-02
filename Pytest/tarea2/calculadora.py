def sum(a: int | float, b: int | float) -> int | float:
    return a + b

def sub(a: int | float, b: int | float) -> int | float:
    return a - b

def mul(a: int | float, b: int | float) -> int | float:
    return a * b

def div(a: int | float, b: int | float) -> int | float:
    return a // b if not isinstance(a, float) or not isinstance(b, float) else a / b

def pow(a: int | float, b: int | float) -> int | float:
    return a ** b