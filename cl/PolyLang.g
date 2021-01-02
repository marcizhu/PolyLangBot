grammar PolyLang;

prog
    : (expr NEWLINE)* EOF
    | expr EOF;

expr: 'color' IDENTIFIER ',' COLOR
    | PRINT (expr | STRING)
    | AREA expr
    | PERIMETER expr
    | VERTICES expr
    | CENTROID expr
    | EQUAL expr ',' expr
    | INSIDE expr ',' expr
    | DRAW STRING ',' expr+
    | expr UNION expr
    | expr INTERSECTION expr
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

PRINT: 'print' ;
AREA: 'area' ;
PERIMETER: 'perimeter' ;
VERTICES: 'vertices' ;
CENTROID: 'centroid' ;
EQUAL: 'equal' ;
INSIDE: 'inside' ;
DRAW: 'draw' ;
ASSIGNMENT: ':=' ;

UNION: '+' ;
INTERSECTION: '*' ;
BOUNDING_BOX: '#' ;
RANDOM_SAMPLE: '!' ;

IDENTIFIER: [A-Za-z] [A-Za-z_$0-9]* ;

STRING: '"' ( '\\' [\\"] | ~[\\"\r\n] )* '"';

NUMBER: [0-9]+ ;

REAL: [0-9]+ '.' [0-9]+
    | '.' [0-9]+
    | [0-9]+ ;

COLOR: '{' REAL REAL REAL '}' ;

POINT: REAL REAL;

NEWLINE : [\r\n]+ ;

LINE_COMMENT: '//' ~[\r\n]* -> skip ;

WS : [ \n]+ -> skip ;
