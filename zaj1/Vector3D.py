from math import sqrt
from __future__ import annotations

class Vector3D:
    def __init__(self, x: float, y:float, z:float):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return f'Vector3D({self.x}, {self.y}, {self.z})'

    def norma(self) -> float:
        return sqrt(self.x**2 + self.y**2, + self.z**2)

    def __add__(self, other: Vector3D) -> Vector3D:
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: Vector3D) -> Vector3D:
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, k: float) -> Vector3D:
        return Vector3D(self.x * k, self.y * k, self.z * k)

    @staticmethod
    def dot(self, other: Vector3D) -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z
    @staticmethod
    def cross(self, other: Vector3D) -> Vector3D:
        return Vector3D(self.y * other.z - self.z * other.y,
                        self.z * other.x - self.x * other.z,
                        self.x * other.y - self.y * other.x)

    def are_orthogonal(self, other: Vector3D) -> bool:
        return self.dot(self, other) == 0


