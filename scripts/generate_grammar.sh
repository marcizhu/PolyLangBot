#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

cd "$DIR/../tools"
java -jar antlr-4.9.1-complete.jar -Dlanguage=Python3 -no-listener -visitor ../cl/PolyLang.g

cd "$DIR/../cl"
rm PolyLang.interp
rm PolyLang.tokens
rm PolyLangLexer.interp
rm PolyLangLexer.tokens
