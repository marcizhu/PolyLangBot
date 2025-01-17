import functools  # functools.reduce()
import math       # math.atan2()
import random     # random.uniform()

from PIL import Image, ImageDraw  # Image drawing functions


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Point(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        return Point(self.x / other.x, self.y / other.y)

    def __lt__(self, other):
        return self.x < other.x or (self.x == other.x and self.y < other.y)

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return self.x > other.x or (self.x == other.x and self.y > other.y)

    def __ge__(self, other):
        return self > other or self == other

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

    def __str__(self):
        return "({:.3f}, {:.3f})".format(self.x, self.y)

    def scale(self, k):
        return Point(k * self.x, k * self.y)

    @property
    def magnitude(self):
        return (self.x * self.x + self.y * self.y)**0.5

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y * other.x


class ConvexPolygon:
    def __init__(self, points=[], color=(0, 0, 0)):
        """Creates a new convex polygon that contains all the given points

        Parameters
        ----------
        points : list
            List of points in the format [[x0, y0], [x1, y1], ... [xn, yn]] that this polygon will contain
        color : color
            Color of this polygon by default. It defaults to black
        """
        self.__points = self.__convex_hull(points)
        self.color = color

    def __str__(self):
        if len(self.__points) == 0:
            return "{}"
        return "{" + ", ".join(str(p) for p in [self.__points[0]] + list(reversed(self.__points[1:]))) + "}"

    def __iter__(self):
        """Return points in the polygon in order"""
        for p in [self.__points[0]] + list(reversed(self.__points[1:])):
            yield p

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__points == other.__points
        else:
            return False

    def __segments(self):
        """Returns a list of points like the following: [[x0, y0], [x1, y1], [x2, y2], ..., [xn, yn], [x0, y0]]"""
        if len(self.__points) == 0:
            return []

        return zip(self.__points, self.__points[1:] + [self.__points[0]])

    def area(self):
        """Returns the area of the polygon"""
        return 0.5 * abs(sum(p0.cross(p1) for (p0, p1) in self.__segments()))

    def perimeter(self):
        """Returns the perimeter of the polygon"""
        # Uses Pythagoras' Theorem to calculate distance between all adjacent points, then adds them up
        return sum([(p0 - p1).magnitude for (p0, p1) in self.__segments()])

    def centroid(self):
        """Returns the centroid of this polygon"""
        A = self.area()
        x = sum([(p0.x + p1.x) * p0.cross(p1) for (p0, p1) in self.__segments()]) / (6 * A)
        y = sum([(p0.y + p1.y) * p0.cross(p1) for (p0, p1) in self.__segments()]) / (6 * A)
        return Point(x, y)

    def bounding_box(self):
        """Returns the Axis-aligned Bounding Box (AABB) of this polygon"""
        x_coord = [p.x for p in self.__points]
        y_coord = [p.y for p in self.__points]

        x_min = min(x_coord)
        x_max = max(x_coord)
        y_min = min(y_coord)
        y_max = max(y_coord)

        return ConvexPolygon([Point(x_min, y_min), Point(x_max, y_min), Point(x_max, y_max), Point(x_min, y_max)])

    def union(self, other):
        """Computes the convex union of this and the other given polygons"""
        return ConvexPolygon(self.__points + other.__points)

    def intersection(self, other):
        """Compute the intersection between two polygons, self and other"""
        # Sutherland–Hodgman Polygon Clipping Algorithm
        def inside(p):
            return (cp2.x - cp1.x) * (p.y - cp1.y) >= (cp2.y - cp1.y) * (p.x - cp1.x)

        def computeIntersection(cp1, cp2, e, s):
            dc = cp1 - cp2
            dp = s - e
            n1 = cp1.cross(cp2)
            n2 = s.cross(e)
            n3 = 1.0 / (dc.cross(dp))
            return Point((n1 * dp.x - n2 * dc.x) * n3, (n1 * dp.y - n2 * dc.y) * n3)

        outputList = self.__points
        cp1 = other.__points[-1]

        for clipVertex in other.__points:
            cp2 = clipVertex
            inputList = outputList
            outputList = []
            s = inputList[-1]

            for subjectVertex in inputList:
                e = subjectVertex
                if inside(e):
                    if not inside(s):
                        outputList.append(computeIntersection(cp1, cp2, e, s))
                    outputList.append(e)

                elif inside(s):
                    outputList.append(computeIntersection(cp1, cp2, e, s))
                s = e
            cp1 = cp2

        return ConvexPolygon(outputList)

    def get_vertices(self):
        """Returns the list of vertices of this polygon"""
        return self.__points

    def set_vertices(self, points):
        """Sets thhe vertices for this polygon"""
        self.__points = self.__convex_hull(points)

    # Property to access vertices
    vertices = property(get_vertices, set_vertices)

    def is_regular(self):
        """Returns True if polygon is regular, False otherwise"""
        def angles_are_equal(self):
            if len(self.__points) <= 2:
                return False

            angles = set()
            for p1, ref, p2 in zip(self.__points, self.__points[1:] + [self.__points[0]], self.__points[2:] + self.__points[:2]):
                v1 = p1 - ref
                v2 = p2 - ref

                dot = v1.dot(v2)      # dot product
                cross = v1.cross(v2)  # cross product
                angles.add(math.atan2(cross, dot))

            return len(angles) == 1

        def sides_are_equal(self):
            return len(set([(p0 - p1).magnitude for (p0, p1) in self.__segments()])) == 1

        return angles_are_equal(self) and sides_are_equal(self)

    def draw(self, img, aabb=None):
        """Draws this polygon into the given image

        Draws this polygon on the given image using the polygon's color and, op-
        tionally, rescaling the poligon to the given bounding box. The resulting
        image contains the polygon, with the given AABB centered and with the
        least possible amount of whhitespace around it.

        Parameters
        ----------
        img : PIL.Image
            Image where this polygon will be drawn
        aabb : ConvexPolygon (optional)
            Bounding box of the image. This polygon will be used to rescale the
            poligon so that multiple polygons can be drawn on the same image. Set
            to None (or don't pass anything) if you want to draw this polygon as
            big as possible.
        """
        if aabb is None:
            aabb = self.bounding_box()

        dib = ImageDraw.Draw(img)

        x_coord = [p.x for p in aabb.__points]
        y_coord = [p.y for p in aabb.__points]

        x_min = min(x_coord)
        y_min = min(y_coord)
        x_max = max(x_coord) - x_min
        y_max = max(y_coord) - y_min

        biggest = max(x_max, y_max)
        x_free = (biggest - x_max) / 2
        y_free = (biggest - y_max) / 2

        def rescale(p):
            pt = (p - Point(x_min, y_min) + Point(x_free, y_free)) / Point(biggest, biggest) * Point(img.width - 5, img.height - 5) + Point(2, 2)
            return (pt.x, pt.y)

        pts = [rescale(p) for p in self.__points]
        dib.polygon(pts, self.color)

    @property
    def n_vertices(self):
        """Returns the number of vertices of this polygon"""
        return len(self.__points)

    @property
    def n_edges(self):
        """Returns the number of edges of this polygon"""
        if len(self.__points) == 1 or len(self.__points) == 2:
            return len(self.__points) - 1

        return len(self.__points)

    def contains(self, point):
        """Checks whether the given point or polygon is inside of the polygon"""
        if isinstance(point, self.__class__):
            return all([self.__contains(p) for p in point.__points])
        elif isinstance(point, Point):
            return self.__contains(point)

    def __contains(self, pt):
        """Checks whether the given point is inside of the polygon"""
        for p1, p2 in self.__segments():
            if (p2 - p1).cross(pt - p1) < 0:
                return False

        return True

    @staticmethod
    def __convex_hull(points):
        """Returns points on convex hull in CCW order according to Graham's scan algorithm"""
        TURN_LEFT, TURN_RIGHT, TURN_NONE = (1, -1, 0)

        def cmp(a, b):
            return (a > b) - (a < b)

        def turn(p, q, r):
            return cmp((q.x - p.x) * (r.y - p.y) - (r.x - p.x) * (q.y - p.y), 0)

        def _keep_left(hull, r):
            while len(hull) > 1 and turn(hull[-2], hull[-1], r) == TURN_RIGHT:  # =! TURN_LEFT
                hull.pop()
            if not len(hull) or hull[-1] != r:
                hull.append(r)
            return hull

        points = sorted(points)
        l = functools.reduce(_keep_left, points, [])
        u = functools.reduce(_keep_left, reversed(points), [])
        return l.extend(u[i] for i in range(1, len(u) - 1)) or l
