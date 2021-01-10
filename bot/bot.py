from telegram import ParseMode, ChatAction
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import io  # For io.BytesIO() (aka saving data to memory)
from antlr4 import *
from cl.TreeVisitor import TreeVisitor  # Tree Visitor for this language
from cl.PolyLangLexer import PolyLangLexer
from cl.PolyLangParser import PolyLangParser


def run():
    def handler(update, context):
        """Main message handler. Recieves a message, executes its contents and returns the output"""

        def execute(text, visitor):
            """Executes `text` and returns the output in Markdown format. Uses `visitor` to visit the AST"""
            try:
                lexer = PolyLangLexer(InputStream(text))
                token_stream = CommonTokenStream(lexer)
                parser = PolyLangParser(token_stream)
                tree = parser.prog()
                visitor.visit(tree)
                # Return output inside a code block using Markdown
                return "```\n" + visitor.output + "\n```"
            except Exception as e:
                # \u26A0 is the Unicode code (UTF-8) for the exclamation sign emoji (⚠️)
                # Putting text *between asterisks* makes it bold
                return "*\u26A0 ERROR: Uncaught exception: " + str(e) + " \u26A0*"

        if not update.effective_chat.id in context.bot_data:
            start(update, context)

        # Set the bot status as "Typing..."
        update.effective_chat.send_action(action=ChatAction.TYPING)

        # Execute the recieved text, using the previous TreeVisitor class so that the user can reference
        # previously-created polygons
        ret = execute(update.message.text, context.bot_data[update.effective_chat.id])

        if ret != "```\n\n```":
            # If the execution generated any output, send it to the user
            context.bot.send_message(chat_id=update.effective_chat.id, text=ret, parse_mode=ParseMode.MARKDOWN_V2)

    def img_callback(update, context, img):
        """Image callback. Recieves the image, saves it to memory and sends it through Telegram"""
        with io.BytesIO() as output:
            img.save(output, format="PNG")
            output.seek(0)

            # Set the bot status as "Uploading photo..." & send the image
            update.effective_chat.send_action(action=ChatAction.UPLOAD_PHOTO)
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=output, caption=img.filename)

    def start(update, context):
        """Initializes the bot for the given user"""
        if update.effective_chat.id in context.bot_data:
            del context.bot_data[update.effective_chat.id]
            context.bot.send_message(chat_id=update.effective_chat.id, text="Environment cleared")
        else:
            help_msg(update, context)

        # Create a new TreeVisitor class instance with a custom callback for images. This handler will intercept
        # the image and, instead of saving it to disk like normally, it will save it to memory and send it through
        # Telegram, completely ignoring the path specified. This is both faster and safer, since there is no way
        # to create/overwrite files on the bot's PC using mallicious `draw` commands.
        context.bot_data[update.effective_chat.id] = TreeVisitor(lambda p: img_callback(update, context, p))

    def help_msg(update, context):
        message = "*Welcome to the PolyLang telegram bot*\n\n"

        message += "This is a bot designed to work with convex polygons using a new programming language called PolyLang\. "
        message += "Just type your script as a message, send it and the bot will automatically reply with the "
        message += "generated output\. Here's a small script to begin with:\n\n"

        message += "```\n"
        message += "p0 := [0 0  1 0  0\.5 1]\n"
        message += "color p0, {0\.01 0\.776 1}\n"
        message += "draw \"image\.png\", p0\n"
        message += "```\n\n"

        message += "You can get more information and code examples on this language [here](https://github.com/jordi-petit/lp-polimomis-2020)\."

        context.bot.send_message(chat_id=update.effective_chat.id, text=message, parse_mode=ParseMode.MARKDOWN_V2)

    # Read the private token
    TOKEN = open('bot/token.txt').read().strip()

    # Create Telegram objects
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Create message & command handler
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_msg))
    dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.update.edited_message), handler))

    # Start running
    updater.start_polling()
    input() # Wait for a newline
    print("Exiting...")
    updater.stop()
