import sys
from polygons import *  # Class ConvexPolygon, class Point

from antlr4 import *
from cl.TreeVisitor import TreeVisitor  # Tree Visitor for this language
from cl.PolyLangLexer import PolyLangLexer
from cl.PolyLangParser import PolyLangParser
import bot.bot as bot

def execute(input_stream, visitor):
    try:
        lexer = PolyLangLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = PolyLangParser(token_stream)
        tree = parser.prog()
        visitor.visit(tree)
        print(visitor.output)
    except Exception as e:
        print("ERROR: Uncaught exception:", e)

if __name__ == "__main__":
    if len(sys.argv) == 1 or (len(sys.argv) == 2 and (sys.argv[1] == "-i" or sys.argv[1] == "--interactive")):
        # Run in interactive mode
        print("Welcome to the PolyLang interactive interpreter v0.0.1")
        print("Type your commands followed by an enter to execute them. Press Ctrl+D or Ctrl+C to exit.")

        try:
            visitor = TreeVisitor()
            while True:
                input_stream = InputStream(input(">>> "))
                execute(input_stream, visitor)
        except (EOFError, KeyboardInterrupt):
            print("\nBye bye!")

    elif len(sys.argv) == 2 and (sys.argv[1] == "-b" or sys.argv[1] == "--bot"):
        bot.run()

    elif len(sys.argv) == 2:
        input_stream = FileStream(sys.argv[1])
        execute(input_stream, TreeVisitor())
