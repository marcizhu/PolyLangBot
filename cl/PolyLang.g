grammar PolyLang;

prog
    : expr
    | (expr NEWLINE)*
    | EOF;

expr
    : 'color' IDENTIFIER ',' COLOR
    | 'print' (expr | STRING)
    | 'area' expr
    | 'perimeter' expr
    | 'vertices' expr
    | 'centroid' expr
    | 'equal' expr ',' expr
    | 'inside' expr ',' expr
    | 'draw' STRING ',' expr+
    | '(' expr ')'
    | expr '+' expr
    | expr '*' expr
    | '#' expr
    | '!' NUMBER
    | IDENTIFIER ':=' expr
    | IDENTIFIER
    | POLYGON
    | POINT ;

IDENTIFIER: [A-Za-z] [A-Za-z_$0-9]* ;

STRING: '"' ([A-Za-z0-9] | ' ' | '\\t' | '\\n' | '\\"' | '.')* '"' ;

NUMBER: [0-9]+ ;

REAL: [0-9]+ '.' [0-9]+
    | '.' [0-9]+
    | [0-9]+ ;

COLOR: '{' REAL [ \t]+ REAL [ \t]+ REAL '}' ;

POINT: REAL [ \t]+ REAL ;

POLYGON: '[' POINT ([ \t]+ POINT)* ']' ;

NEWLINE : [\r\n]+ ;

WS : [ \t]+ -> skip ;
