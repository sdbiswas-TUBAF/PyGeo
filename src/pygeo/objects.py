import numpy as np


class Point:
    """A point."""

    def __init__(self, point):
        self._point = np.array(point, dtype=float)

    def __repr__(self):
        return f"Point({self._point.tolist()})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Point(self._point + other._vector)
        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, Vector):
            return Point(other._vector + self._point)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Point):
            return Vector(self._point - other._point)
        return NotImplemented

    def __eq__(self, other):
        print("Inside point")
        if isinstance(other, Point):
            return np.array_equal(other._point, self._point)
        return False


class Vector:
    """A vector."""

    def __init__(self, vector):
        self._vector = np.array(vector, dtype=float)

    def __repr__(self):
        return f"Point({self._vector.tolist()})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self._vector + other._vector)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self._vector - other._vector)
        return NotImplemented
    
    
    def __eq__(self, other):
        print("Inside vector")
        if isinstance(other, Vector):
            return np.array_equal(other._vector, self._vector)
        return False


class Ray:
    """A ray."""

    def __init__(self,origin,direction): 
        self._origin = np.array(origin)
        if np.array_equal(np.array(direction), np.array([0, 0, 0])):
            self._direction = np.array(direction)
        else:
            self._direction = np.array(direction)/np.linalg.norm(np.array(direction))



    def __repr__(self):
        return f"Ray: Point = {self._origin} Direction = {self._direction}"

    def __eq__(self, other):
        if isinstance(other,Ray):
            flag = False
            if np.array_equal(self._origin, other._origin) and np.array_equal(self._direction , other._direction):
                flag = True
            return flag
        return False

class Sphere:
    """A sphere."""
    def __init__(self, center, radius):
        self._center = np.array(center,dtype=float)
        self._radius = float(radius)
    def __repr__(self):
        return f"Sphere(Center:{self._center.tolist()}, Radius:{self._radius})"
    def __eq__(self, other):
        if isinstance(other,Sphere):
            flag = False
            if np.array_equal(other._center, self._center) and (other._radius == self._radius):
                flag = True
            return flag
        return False


class Triangle:
    """A triangle."""