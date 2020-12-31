import functools
import math

# - Check whether a point is inside another convex polygon.
# - Check whether a convex polygon is inside another convex polygon.
# - Check if a convex polygon is regular.
# - Compute the intersection of two convex polygons.
# - Compute the convex union of two convex polygons.
# - Draw convex polygons (with colors) in a PNG image.


# Internal representation of a convex polygon. -> As a list of CCW points in the convex hull
# Specification and documentation of its public operations.
# Private operations.
# Algorithms to perform the required operations efficiently (remember, nlogn is better than n²).
# Set of test examples to check the functionality of the class.

class ConvexPolygon:
    def __init__(self, points = []):
        """
        Creates a new convex polygon that contains all the given points
        """
        self.points = self._convex_hull(points)


    def _segments(self):
        """
        Returns a list of points like the following: [[x0, y0], [x1, y1], [x2, y2], ..., [xn, yn], [x0, y0]]
        """
        return zip(self.points, self.points[1:] + [self.points[0]])


    def area(self):
        """
        Returns the area of the polygon
        """
        return 0.5 * abs(sum(x0 * y1 - x1 * y0 for ((x0, y0), (x1, y1)) in self._segments()))


    def perimeter(self):
        """
        Returns the perimeter of the polygon
        """
        # Uses Pythagoras' Theorem to calculate distance between all adjacent points, then adds them up
        return sum([math.sqrt((x0 - x1) * (x0 - x1) + (y0 - y1) * (y0 - y1)) for ((x0, y0), (x1, y1)) in self._segments()])


    def centroid(self):
        """
        Returns the centroid of this polygon
        """
        A = self.area()
        x = sum([(x0 + x1) * (x0 * y1 - x1 * y0) for ((x0, y0), (x1, y1)) in self._segments()])
        y = sum([(y0 + y1) * (x0 * y1 - x1 * y0) for ((x0, y0), (x1, y1)) in self._segments()])
        return [x / (6 * A), y / (6 * A)]


    def bounding_box(self):
        """
        Returns the Axis-aligned Bounding Box (AABB) of this polygon
        """
        x_coord = [p[0] for p in self.points]
        y_coord = [p[1] for p in self.points]

        x_min = min(x_coord)
        x_max = max(x_coord)
        y_min = min(y_coord)
        y_max = max(y_coord)

        return ConvexPolygon([[x_min, y_min], [x_max, y_min], [x_max, y_max], [x_min, y_max]])


    def get_vertices(self):
        """
        Returns the list of vertices of this polygon
        """
        return self.points
    

    def set_vertices(self, points):
        """
        Sets thhe vertices for this polygon
        """
        self.points = self._convex_hull(points)

    # Property to access vertices
    vertices = property(get_vertices, set_vertices)

    @property
    def n_vertices(self):
        """
        Returns the number of vertices of this polygon
        """
        return len(self.points)


    @property
    def n_edges(self):
        """
        Returns the number of edges of this polygon
        """
        return len(self.points)


    @staticmethod
    def _convex_hull(points):
        """
        Returns points on convex hull in CCW order according to Graham's scan algorithm. 
        """
        TURN_LEFT, TURN_RIGHT, TURN_NONE = (1, -1, 0)

        def cmp(a, b):
            return (a > b) - (a < b)

        def turn(p, q, r):
            return cmp((q[0] - p[0])*(r[1] - p[1]) - (r[0] - p[0])*(q[1] - p[1]), 0)

        def _keep_left(hull, r):
            while len(hull) > 1 and turn(hull[-2], hull[-1], r) == TURN_RIGHT: # =! TURN_LEFT
                hull.pop()
            if not len(hull) or hull[-1] != r:
                hull.append(r)
            return hull

        points = sorted(points)
        l = functools.reduce(_keep_left, points, [])
        u = functools.reduce(_keep_left, reversed(points), [])
        return l.extend(u[i] for i in range(1, len(u) - 1)) or l


if __name__ == "__main__":
    poly = ConvexPolygon()
    poly.vertices = [[0.0, 0.0], [0.0, 1.0], [1.0, 1.0], [1.5, 0.5]]
    print("done")
    print(poly.vertices)
    print(poly.centroid())
    print(poly.area())
    print(poly.perimeter())
