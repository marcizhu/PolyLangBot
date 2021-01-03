from antlr4 import *                            # ANTLR4 Classes
from polygons import *                          # Class ConvexPolygon, Class Point
from cl.PolyLangLexer import PolyLangLexer      # Lexer
from cl.PolyLangParser import PolyLangParser    # Parser
from cl.PolyLangVisitor import PolyLangVisitor  # Visitor


class TreeVisitor(PolyLangVisitor):
    """Visitor class that executes the instructions of the PolyLang language"""

    def __init__(self):
        # Initialize a dictionary to store all polygons
        self.__polygons = {}

    def visitProg(self, ctx: PolyLangParser.ProgContext):
        """Visit all childs of a program (expressions) and print their result"""
        for n in ctx.getChildren():
            try:
                ret = self.visit(n)
                if isinstance(ret, float):
                    print(f"{ret:.3f}")
                elif isinstance(ret, bool):
                    print("yes" if ret else "no")
                elif isinstance(ret, str) or isinstance(ret, int):
                    print(ret)

            except (ReferenceError, SyntaxError) as err:
                print(err)

    def getPolygon(self, identifier):
        """Gets a polygon with the given identifier or raises an exception if it is not defined"""
        if identifier not in self.__polygons:
            raise ReferenceError("ERROR: undefined identifier '" + identifier + "'")

        return self.__polygons[identifier]

    def visitExpr(self, ctx: PolyLangParser.ExprContext):
        """Visit an expression, recursively evaluating it"""
        l = [n for n in ctx.getChildren()]

        if hasattr(l[0], 'getSymbol'):
            token = l[0].getSymbol().type
        elif hasattr(l[1], 'getSymbol'):
            token = l[1].getSymbol().type
        else:
            token = None

        if token == PolyLangParser.LPARENS:
            return self.visit(l[1])

        elif token == PolyLangParser.PRINT:
            if hasattr(l[1], 'getSymbol') and l[1].getSymbol().type == PolyLangParser.STRING:
                return l[1].getText()[1:-1]  # String

            return str(self.visit(l[1]))

        elif token == PolyLangParser.IDENTIFIER:
            if len(l) == 3 and l[1].getSymbol().type == PolyLangParser.ASSIGNMENT:
                # IDENTIFIER ':=' expr
                self.__polygons[l[0].getText()] = self.visit(l[2])
            elif len(l) == 1:
                # IDENTIFIER
                return self.getPolygon(l[0].getText())

        elif token == PolyLangParser.LBRACKET:
            # Constructor
            pts = [str(x) for x in l[1:-1]]
            args = [Point(float(l.split(' ')[0]), float(l.split(' ')[1])) for l in pts]
            return ConvexPolygon(args)

        elif token == PolyLangParser.COLOR:
            def float2int(f):
                return int(float(f) * 255)

            poly = self.getPolygon(l[1].getText())
            colors = l[3].getText()[1:-1].split(' ')
            poly.color = (float2int(colors[0]), float2int(colors[1]), float2int(colors[2]))

        elif token == PolyLangParser.AREA:
            poly = self.visit(l[1])
            return poly.area()

        elif token == PolyLangParser.PERIMETER:
            poly = self.visit(l[1])
            return poly.perimeter()

        elif token == PolyLangParser.VERTICES:
            poly = self.visit(l[1])
            return poly.n_vertices

        elif token == PolyLangParser.EDGES:
            poly = self.visit(l[1])
            return poly.n_edges

        elif token == PolyLangParser.CENTROID:
            poly = self.visit(l[1])
            return str(poly.centroid())

        elif token == PolyLangParser.REGULAR:
            poly = self.visit(l[1])
            return poly.is_regular()

        elif token == PolyLangParser.BOUNDING_BOX:
            poly = self.visit(l[1])
            return poly.bounding_box()

        elif token == PolyLangParser.EQUAL:
            p1 = self.visit(l[1])
            p2 = self.visit(l[3])
            return p1 == p2

        elif token == PolyLangParser.INSIDE:
            p1 = self.visit(l[1])
            p2 = self.visit(l[3])
            return p2.contains(p1)

        elif token == PolyLangParser.DRAW:
            path = l[1].getText()[1:-1]
            polygons = [self.visit(l[n]) for n in range(3, len(l)+1, 2)]
            img = Image.new('RGB', (400, 400), 'White')

            aabb = ConvexPolygon()
            for poly in polygons:
                aabb = aabb.union(poly)

            for poly in polygons:
                poly.draw(img, aabb)

            img = img.transpose(Image.FLIP_TOP_BOTTOM)
            img.save(path)

        elif token == PolyLangParser.RANDOM_SAMPLE:
            count = int(l[1].getText())
            points = [Point(random.uniform(0, 1), random.uniform(0, 1)) for n in range(count)]
            return ConvexPolygon(points)

        elif token == PolyLangParser.UNION:
            p1 = self.visit(l[0])
            p2 = self.visit(l[2])
            return p1.union(p2)

        elif token == PolyLangParser.INTERSECTION:
            p1 = self.visit(l[0])
            p2 = self.visit(l[2])
            return p1.intersection(p2)

        else:
            raise SyntaxError("ERROR: Unknown token")
