age: int = 5
name: str = "Max"

def add(a: int, b:int) -> int:
    return a + b


print(add(3, 3))

# add("3", "3") i tak zadziała, ale zwróci "33"