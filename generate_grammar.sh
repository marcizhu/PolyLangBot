#!/bin/bash

cd cl
java -jar antlr-4.7.1-complete.jar -Dlanguage=Python3 -no-listener -visitor PolyLang.g
