# importa l'API de Telegram
from telegram.ext import Updater, MessageHandler, Filters

from antlr4 import *
from cl.TreeVisitor import TreeVisitor  # Tree Visitor for this language
from cl.PolyLangLexer import PolyLangLexer
from cl.PolyLangParser import PolyLangParser


def run():
    def handler(update, context):
        """Main message handler. Recieves a message, executes its contents and returns the output"""

        def img_callback(update, context, path):
            """Image callback. Recieves a path and sends that image through Telegram"""
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(path, 'rb'), caption=path)

        def execute(text, visitor):
            """Executes `text` and returns the output. Uses `visitor` to visit the AST"""
            try:
                lexer = PolyLangLexer(InputStream(text))
                token_stream = CommonTokenStream(lexer)
                parser = PolyLangParser(token_stream)
                tree = parser.prog()
                visitor.visit(tree)
                return visitor.output
            except Exception as e:
                return "ERROR: Uncaught exception: " + str(e)

        if not update.effective_chat.id in context.bot_data:
            context.bot_data[update.effective_chat.id] = TreeVisitor(lambda p: img_callback(update, context, p))

        ret = execute(update.message.text, context.bot_data[update.effective_chat.id])

        if ret != "":
            context.bot.send_message(chat_id=update.effective_chat.id, text=ret)

    # Read the private token
    TOKEN = open('bot/token.txt').read().strip()

    # crea objectes per treballar amb Telegram
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Create message handler
    dispatcher.add_handler(MessageHandler(Filters.text, handler))

    # Start running
    updater.start_polling()
