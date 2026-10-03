def surface_area_of_cube(edge_length: float) -> str:
    return f"The surface area of the cuve is {6 * edge_length ** 2}."


type Vector = list[float]

def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]

new_vector = scale(2.0, [1.0, -4.2, 5.4])

# Use the NewType helper to create distinct types
from typing import NewType
UserId = NewType('UserId', int)
some_id = UserId(524313)
