from .objects import Point, Ray, Sphere, Triangle, Vector
import numpy as np

def intersect(first_object, second_object):
    """ General method for intersection of objects
      Inputs are : first_object, second_object (PyGeo objects) """

    if isinstance(first_object , Ray) and isinstance(second_object, Sphere):
        return _intersect_ray_with_sphere(first_object,second_object)
    return NotImplemented
      


def _intersect_ray_with_sphere(ray, sphere):
    """Intersection of a Ray(origin, direction) and a Sphere( center, direction).
        returns: 0 for no interceptions
                 NumPy array of coordinates for intersections"""
    diff_o_c = np.subtract(ray._origin,sphere._center)
    delta = (np.dot(ray._direction,diff_o_c))**2 - ((np.dot(diff_o_c,diff_o_c)) - sphere._radius**2)
    if delta < 0:
        print("Specified ray and sphere do not intersect")
        return None
    elif delta == 0:
        d = -1*np.dot(ray._direction,diff_o_c)
        return Point((ray._origin) + (d*ray._direction))
    else:
        d = np.array([-1*np.dot(ray._direction,diff_o_c)-np.sqrt(delta),-1*np.dot(ray._direction,diff_o_c)+np.sqrt(delta)])
        coordinates = []
        for d in d[d>=0]:
            coordinates.append(Point((ray._origin) + (d*ray._direction)))
        return np.array(coordinates)