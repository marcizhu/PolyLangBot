grammar PolyLang;

prog: (expr NEWLINE*)* ;

expr: COLOR IDENTIFIER ',' COLOR_RGB
    | expr UNION expr
    | expr INTERSECTION expr
    | PRINT (expr | STRING)
    | AREA expr
    | CENTROID expr
    | EDGES expr
    | PERIMETER expr
    | REGULAR expr
    | VERTICES expr
    | EQUAL expr ',' expr
    | INSIDE expr ',' expr
    | DRAW STRING (',' expr)+
    | BOUNDING_BOX expr
    | RANDOM_SAMPLE NUMBER
    | LPARENS expr RPARENS
    | IDENTIFIER ASSIGNMENT expr
    | LBRACKET POINT* RBRACKET
    | IDENTIFIER ;

LPARENS: '(' ;
RPARENS: ')' ;

LBRACE: '{' ;
RBRACE: '}' ;

LBRACKET: '[' ;
RBRACKET: ']' ;

AREA: 'area' ;
CENTROID: 'centroid' ;
COLOR: 'color' ;
DRAW: 'draw' ;
EDGES: 'edges' ;
EQUAL: 'equal' ;
INSIDE: 'inside' ;
PERIMETER: 'perimeter' ;
PRINT: 'print' ;
REGULAR: 'regular' ;
VERTICES: 'vertices' ;

ASSIGNMENT: ':=' ;
UNION: '+' ;
INTERSECTION: '*' ;
BOUNDING_BOX: '#' ;
RANDOM_SAMPLE: '!' ;

IDENTIFIER: [A-Za-z] [A-Za-z_$0-9]* ;

STRING: '"' ( '\\' [nt] | [\\"] | ~[\\"\r\n] )* '"';

NUMBER: [0-9]+ ;

REAL: ('-'|'+')? [0-9]+ '.' [0-9]+
    | ('-'|'+')? '.' [0-9]+
    | ('-'|'+')? [0-9]+ ;

COLOR_RGB: '{' REAL WS REAL WS REAL '}' ;

POINT: REAL WS REAL;

NEWLINE : [\r\n]+ ;

LINE_COMMENT: '//' ~[\r\n]* NEWLINE* -> skip ;

WS : [ \t\n]+ -> skip ;
