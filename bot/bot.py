from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from antlr4 import *
from cl.TreeVisitor import TreeVisitor  # Tree Visitor for this language
from cl.PolyLangLexer import PolyLangLexer
from cl.PolyLangParser import PolyLangParser


def run():
    def handler(update, context):
        """Main message handler. Recieves a message, executes its contents and returns the output"""

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
            start(update, context)

        # Execute the recieved text, using the previous TreeVisitor class so that the user can reference
        # previously-created polygons
        ret = execute(update.message.text, context.bot_data[update.effective_chat.id])

        if ret != "":
            # If the execution generated any output, send it to the user
            context.bot.send_message(chat_id=update.effective_chat.id, text=ret)

    def img_callback(update, context, img):
        """Image callback. Recieves a path and sends that image through Telegram"""
        img.save("telegram-bot.png")  # Override the filename for security reasons.
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open("telegram-bot.png", 'rb'), caption=img.filename)

    def start(update, context):
        """Initializes the bot for the given user"""
        if update.effective_chat.id in context.bot_data:
            del context.bot_data[update.effective_chat.id]
            context.bot.send_message(chat_id=update.effective_chat.id, text="Environment cleared")

        # Create a new TreeVisitor class instance with a custom callback for images. This handler will override
        # the path where the image will be saved to "telegram-bot.png" independently of what the user specified.
        # This is mainly done for two reasons:
        # 1) To prevent filling up my hard disk with random images
        # 2) For security reasons. This way, we are safe against mallicious `draw` commands like the following:
        #
        #   draw "C:\Windows\System32\kernel32.dll", [0 0 1 1]
        #
        # This command would normally overwrite a system file, but because we override its name, it will be
        # saved to "telegram-bot.png" regardless of the path specified.
        context.bot_data[update.effective_chat.id] = TreeVisitor(lambda p: img_callback(update, context, p))

    # Read the private token
    TOKEN = open('bot/token.txt').read().strip()

    # Create Telegram objects
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Create message & command handler
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.update.edited_message), handler))

    # Start running
    updater.start_polling()
    input() # Wait for a newline
    print("Exiting...")
    updater.stop()
