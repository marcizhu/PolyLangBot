grammar PolyLang;

prog
    : (expr NEWLINE)* EOF
    | expr EOF;

expr: 'color' IDENTIFIER ',' COLOR
    | PRINT (expr | STRING)
    | AREA expr
    | PERIMETER expr
    | VERTICES expr
    | EDGES expr
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
EDGES: 'edges' ;
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

COLOR: '{' REAL WS REAL WS REAL '}' ;

POINT: REAL WS REAL;

NEWLINE : [\r\n]+ -> skip ;

LINE_COMMENT: '//' ~[\r\n]* -> skip ;

WS : [ \t\n]+ -> skip ;
