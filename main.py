from polygons import * # Convex Polygon class

from antlr4 import *
from cl.TreeVisitor import TreeVisitor # Tree Visitor for this language
from cl.PolyLangLexer import PolyLangLexer
from cl.PolyLangParser import PolyLangParser

if __name__ == "__main__":
    """
    poly     = ConvexPolygon([Point(0.0, 0.0), Point(0.0, 1.0), Point(1.0, 1.0), Point(1.5, 0.5)])
    square   = ConvexPolygon([Point(1.0, 1.0), Point(2.0, 1.0), Point(1.0, 2.0), Point(2.0, 2.0)])
    triangle = ConvexPolygon([Point(2.5, 2.5), Point(7.5, 2.5), Point(5.0, 5.0)])
    p1       = ConvexPolygon([Point(0.0, 0.0), Point(0.0, 1.0), Point(1.0, 1.0), Point(0.2, 0.8)])

    print(p1)
    print(p1.area())
    print(p1.perimeter())
    print(p1.n_vertices)
    print(p1.centroid())

    print("---")

    p2 = ConvexPolygon([Point(0.0, 0.0), Point(1.0, 0.0), Point(1.0, 1.0)])
    print(p2)
    print("yes" if p2.contains(p1) else "no")
    print("yes" if p2.contains(Point(0.8, 0.2)) else "no")

    print("poly = ", poly)
    print(poly.centroid())
    print(poly.area())
    print(poly.perimeter())
    print(poly.is_regular())
    print(square.is_regular())
    print("Point (1.5, 1.5) is inside: ", square.contains(Point(1.5, 1.5)))
    print("Point (2.5, 1.5) is inside: ", square.contains(Point(2.5, 1.5)))
    print("Point (1.5, 2.5) is inside: ", square.contains(Point(1.5, 2.5)))
    print("Point (0.5, 0.5) is inside: ", square.contains(Point(0.5, 0.5)))
    print("Point (2.0, 2.0) is inside: ", square.contains(Point(2.0, 2.0)))

    img = Image.new('RGB', (400, 400), 'White')

    aabb = poly          \
        .union(triangle) \
        .union(square)

    print(aabb.contains(square))
    print(aabb.contains(Point(10.5, 1.5)))

    aabb.color = 'Pink'
    poly.color = 'Green'
    triangle.color = 'Blue'
    square.color = (255, 0, 0)

    aabb.draw(img)
    poly.draw(img, aabb)
    triangle.draw(img, aabb)
    square.draw(img, aabb)
    img = img.transpose(Image.FLIP_TOP_BOTTOM)
    img.save('test-img.png')

    print("-------------------")
    """
    visitor = TreeVisitor()

    #try:
    #while True:
    input_stream = FileStream("examples/sample.poly") #InputStream(input(">>> ")) #FileStream("test.poly")
    lexer = PolyLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = PolyLangParser(token_stream)
    tree = parser.prog()
    visitor.visit(tree)
    #except:
    print("\nBye bye")
