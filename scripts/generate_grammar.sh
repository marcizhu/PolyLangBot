#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

cd "$DIR/../cl"
java -jar antlr-4.7.1-complete.jar -Dlanguage=Python3 -no-listener -visitor PolyLang.g
