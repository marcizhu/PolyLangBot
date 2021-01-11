# PolyLang

An interpreter written in Python for [PolyLang](https://github.com/jordi-petit/lp-polimomis-2020), a programming language designed to work with convex polygons.


## Getting Started

The interpreter can run in three modes:

- **Interactive mode**, where it reads an instruction from keyboard, runs it, and prints the result to the console, similar to what `python -i` does.
- **Script mode**, where it reads a file, executes its contents and prints the result to the terminal.
- **Bot mode**, where it reads commands from telegram, executes them and replies with the output generated.


### Run in interactive mode
To run it in this mode, run `python3 main.py --interactive` or `python3 main.py -i` for short. You should see a small prompt. Type your commands, followed by a new line, and the interpreter will execute the instructions and output the result. For example, try this:

```
>>> print "Hello, world!"
Hello, world!
>>> 
```

### Run in script mode
Several sample scripts are given inside the `examples/` folder. Feel free to run any of them. For example, to execute `examples/sample.poly`, do: `python3 main.py examples/sample.poly`. You should see an output similar to this:

```
{(0.000, 0.000), (0.000, 1.000), (1.000, 1.000)}
0.500
3.414
3
(0.333, 0.667)
---
{(0.000, 0.000), (1.000, 1.000), (1.000, 0.000)}
no
no
yes
---
{(0.000, 0.000), (0.000, 1.000), (1.000, 1.000), (1.000, 0.000)}
{(0.000, 0.000), (1.000, 1.000)}
{(0.000, 0.000), (0.000, 1.000), (1.000, 1.000), (1.000, 0.000)}
yes
```

Also, a new image should have appeared in your folder, called `image.png`. It should look like this:
![](image.png)

### Run in bot mode
To run the interpreter in top mode, you first need to put your Telegram API access token inside a file called `token.txt`. This file should be located inside the folder `bot/`. After that, you can do `python3 main.py --bot` or `python3 main.py -b` for short.

The bot is available at https://t.me/PolyLang_bot and it works just like in iterpreter mode: you type a command, the bot reads it, executes it and sends a message with the output. The polygons are saved between messages, so it is possible to use polygons defined in previously sent messages. Also, each chat has its own isolated environment, so it is impossible for different users to interfere with each other.

Please note that, for security reasons, any `draw` command issued through the Telegram API will **NOT** save the image in the computer's hard drive. Instead, it will save the file to memory and send it through Telegram (with the given file path as caption), both to prevent the host hard drive from filling up and also as a security feature in order to prevent accidental or intentional overwriting of the host files. This approach is faster and safer, since the bot is immune to mallicious `draw` commands like:

```
draw "C:\Windows\System32\Kernel32.dll", [0 0 1 1]
```

Finally, while the bot is processing a command, it will appear as "typing" on Telegram. It will also appear as "Uploading image" while the image is being sent. This feature aims to give more insight to the end user on what the bot is actually doing.


## Prerequisites

This project require `python-telegram-bot`, `antlr4-python3-runtime` and `pillow`. To intall all of them, you can use `pip`:

```
pip3 install -r requirements.txt
```


## Authors

This project was entirely developed by Marc "marcizhu" Izquierdo as an assignment for the Programming Languages course on UPC-FIB.


## License
Copyright (c) 2021 Marc Izquierdo  
This library is licensed under the [MIT License](https://choosealicense.com/licenses/mit/). See
[LICENSE](https://github.com/marcizhu/PolyLangBot/blob/master/LICENSE) for more details.
