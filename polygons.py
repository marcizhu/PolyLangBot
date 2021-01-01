import functools # functools.reduce()
import math      # math.sqrt()

from PIL import Image, ImageDraw # Image drawing functions

# - Check whether a point is inside another convex polygon.
# - Check whether a convex polygon is inside another convex polygon.
# - Compute the intersection of two convex polygons.

# Internal representation of a convex polygon. -> As a list of CCW points in the convex hull
# Specification and documentation of its public operations.
# Private operations.
# Algorithms to perform the required operations efficiently (remember, nlogn is better than n²).
# Set of test examples to check the functionality of the class.

class ConvexPolygon:
    def __init__(self, points = []):
        """Creates a new convex polygon that contains all the given points"""

        self.points = self.__convex_hull(points)


    def __segments(self):
        """Returns a list of points like the following: [[x0, y0], [x1, y1], [x2, y2], ..., [xn, yn], [x0, y0]]"""

        return zip(self.points, self.points[1:] + [self.points[0]])


    def area(self):
        """Returns the area of the polygon"""

        return 0.5 * abs(sum(x0 * y1 - x1 * y0 for ((x0, y0), (x1, y1)) in self.__segments()))


    def perimeter(self):
        """Returns the perimeter of the polygon"""

        # Uses Pythagoras' Theorem to calculate distance between all adjacent points, then adds them up
        return sum([math.sqrt((x0 - x1)**2 + (y0 - y1)**2) for ((x0, y0), (x1, y1)) in self.__segments()])


    def centroid(self):
        """Returns the centroid of this polygon"""

        A = self.area()
        x = sum([(x0 + x1) * (x0 * y1 - x1 * y0) for ((x0, y0), (x1, y1)) in self.__segments()])
        y = sum([(y0 + y1) * (x0 * y1 - x1 * y0) for ((x0, y0), (x1, y1)) in self.__segments()])
        return [x / (6 * A), y / (6 * A)]


    def bounding_box(self):
        """Returns the Axis-aligned Bounding Box (AABB) of this polygon"""

        x_coord = [p[0] for p in self.points]
        y_coord = [p[1] for p in self.points]

        x_min = min(x_coord)
        x_max = max(x_coord)
        y_min = min(y_coord)
        y_max = max(y_coord)

        return ConvexPolygon([[x_min, y_min], [x_max, y_min], [x_max, y_max], [x_min, y_max]])


    def union(self, other):
        """Computes the convex union of this and the other given polygons"""

        return ConvexPolygon(self.points + other.points)


    def get_vertices(self):
        """Returns the list of vertices of this polygon"""

        return self.points
    

    def set_vertices(self, points):
        """Sets thhe vertices for this polygon"""

        self.points = self.__convex_hull(points)

    # Property to access vertices
    vertices = property(get_vertices, set_vertices)


    def is_regular(self):
        """Returns True if polygon is regular, False otherwise"""

        def angles_are_equal(self):
            angles = set()
            for i in range(len(self.points)):
                p1  = self.points[i]
                ref = self.points[i - 1]
                p2  = self.points[i - 2]
                x1, y1 = p1[0] - ref[0], p1[1] - ref[1]
                x2, y2 = p2[0] - ref[0], p2[1] - ref[1]

                numer = (x1 * x2 + y1 * y2)
                denom = math.sqrt((x1**2 + y1**2) * (x2**2 + y2**2))
                angle = math.acos(numer / denom)
                angles.add(angle)

            return len(angles) == 1

        def sides_are_equal(self):
            return len(set([math.sqrt((x0 - x1)**2 + (y0 - y1)**2) for ((x0, y0), (x1, y1)) in self.__segments()])) == 1

        return angles_are_equal(self) and sides_are_equal(self)


    def draw(self, img, color, aabb = None):
        """Draws this polygon into the given image

        Draws this polygon oon the given image using the given color and,
        optionally, rescaling the poligon to the given bounding box.

        Parameters
        ----------
        img : PIL.Image
            Image where this polygon will be drawn
        color : str
            String containing the color of the polygon to paint
        aabb : ConvexPolygon (optional)
            Bounding box of the image. This polygon will be used to rescale the
            poligon so that multiple polygons can be drawn on the same image.
            Set to None (or don't pass anything) if you want to draw this polygon
            as big as possible.
        """

        dib = ImageDraw.Draw(img)

        if aabb == None:
            aabb = self.bounding_box()

        flatten = lambda l: sum(l, [])
        x_min = min(flatten(aabb.points))
        x_max = max(flatten(aabb.points))

        rescale = lambda x, w: (x - x_min) / (x_max - x_min) * (w  - 5) + 2
        pts = [(rescale(x, img.width), rescale(y, img.height)) for x,y in self.points]
        dib.polygon(pts, color)


    @property
    def n_vertices(self):
        """Returns the number of vertices of this polygon"""

        return len(self.points)


    @property
    def n_edges(self):
        """Returns the number of edges of this polygon"""

        return len(self.points)


    @staticmethod
    def __convex_hull(points):
        """Returns points on convex hull in CCW order according to Graham's scan algorithm. """

        TURN_LEFT, TURN_RIGHT, TURN_NONE = (1, -1, 0)

        def cmp(a, b):
            return (a > b) - (a < b)

        def turn(p, q, r):
            return cmp((q[0] - p[0]) * (r[1] - p[1]) - (r[0] - p[0]) * (q[1] - p[1]), 0)

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
    triangle = ConvexPolygon([[2.5, 2.5], [7.5, 2.5], [5.0, 5.0]])
    square = ConvexPolygon([[1.0, 1.0], [2.0, 1.0], [1.0, 2.0], [2.0,2.0]])
    
    print(poly.vertices)
    print(poly.centroid())
    print(poly.area())
    print(poly.perimeter())
    print(poly.is_regular())
    print(square.is_regular())

    img = Image.new('RGB', (400, 400), 'White')
    
    aabb = poly          \
        .union(triangle) \
        .union(square)
    
    aabb.draw(img, 'Pink')
    poly.draw(img, 'Green', aabb)
    triangle.draw(img, 'Blue', aabb)
    square.draw(img, 'Red', aabb)
    img = img.transpose(Image.FLIP_TOP_BOTTOM)
    img.save('test-img.png')
