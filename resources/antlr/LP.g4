grammar LP;
prog:	objective_region constraint_region bound_region ((generals_region? binaries_region?) | (binaries_region? generals_region?)) eof;
objective_region: LF* direction NEWLINE+ obj NEWLINE?;
constraint_region: ST (NEWLINE+ cstr)+ NEWLINE?;
bound_region: BOUNDS (NEWLINE+ bound)+ NEWLINE?;
var_name: NAME;
cstr_name: NAME;
direction: (MAXIMIZE | MINIMIZE) ;
binaries_region: BINARIES (NEWLINE+ var_name+)+ NEWLINE?;
generals_region: GENERALS (NEWLINE+ var_name+)+ NEWLINE?;
expr:	MINUS? (NEWLINE*? term NEWLINE*? (PLUS | MINUS))*? term;
naming: cstr_name ':' ;
cstr: naming? expr NEWLINE*? sense NEWLINE*? NUMBER;
obj: naming? expr ;
eof: END LF* EOF ;
term: NUMBER | (NUMBER NEWLINE*? var_name) | var_name ;
bound: twosided_bound | onesided_bound | bound_free;
onesided_bound: (num_or_inf sense var_name) | (var_name sense num_or_inf) ;
twosided_bound: num_or_inf NEWLINE*? sense NEWLINE*? var_name NEWLINE*? sense NEWLINE*? num_or_inf;
bound_free: var_name NEWLINE*? 'free';
num_or_inf : NUMBER |  INF | (MINUS INF) ;
sense:  LEQ | EQ | GEQ ;

fragment DIGIT : [0-9] ;
fragment M          : ('M'|'m') ;
fragment A          : ('A'|'a') ;
fragment X          : ('X'|'x') ;
fragment I          : ('I'|'i') ;
fragment Z          : ('Z'|'z') ;
fragment E          : ('E'|'e') ;
fragment N          : ('N'|'n') ;
fragment S          : ('S'|'s') ;
fragment U          : ('U'|'u') ;
fragment B          : ('B'|'b') ;
fragment J          : ('J'|'j') ;
fragment C          : ('C'|'c') ;
fragment T          : ('T'|'t') ;
fragment O          : ('O'|'o') ;
fragment D          : ('D'|'d') ;
fragment Y          : ('Y'|'y') ;
fragment F          : ('F'|'f') ;
fragment R          : ('R'|'r') ;
fragment G          : ('G'|'g') ;
fragment L          : ('L'|'l') ;

LF: ( '\r'? '\n' | '\r' | '\f' )+;
MAXIMIZE: LF? ((M A X I M I Z E) | (M A X));
MINIMIZE: LF? ((M I N I M I Z E) | (M I N));
BOUNDS: LF B O U N D S;
BINARIES: LF ((B I N) | (B I N A R Y) | (B I N A R I E S));
GENERALS: LF ((G E N E R A L S) | (G E N E R A L) | (G E N));
ST: LF ((S U B J E C T ' ' T O) | (S T)) ;
END: LF E N D ;
INF: (I N F I N I T Y) | (I N F) ;

COMMENT: '\\'~([\r\n\f])* -> skip;
NEWLINE : (LF SPACES?)+ SPACES+;
NUMBER : MINUS? DIGIT+ ([.] DIGIT+)?  ;
PLUS: '+' ;
MINUS: '-' ;
LEQ: '<=' | '<' | '=<';
GEQ: '>=' |  '>' | '=>';
EQ: '=' ;

fragment NAMESTART
 : '_'
 | [a-zA-Z]
 | '!' | '"' | '#' | '$' | '%' | '&' | '(' | ')' | ',' | ';' | '?' | '@' | '`' | '\'' | '{' | '}' | '~'
 //| [\p{Other_ID_Start}]
 ;
 fragment NAMECONT
 : NAMESTART
 | [0-9] | '.'
 //| [\p{Other_ID_Start}]
 ;
//NONSTARTINGCHAR: [a-zA-Z!"#$%&(),;?@_`'{}~] ;
//CHAR: [a-zA-Z0-9!"#$%&(),.;?@_`'{}~] ;
NAME: NAMESTART NAMECONT*;
SPACES : [ \t]+ -> skip ;

