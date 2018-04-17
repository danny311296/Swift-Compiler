
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'NUMBER ID WHITESPACE ENTER EQ COL PLUS MINUS TIMES DIVIDE LPAREN RPAREN LBRACE RBRACE ARROW COMMA TRIPLEDOT TYPE FOR TYPE FUNC IN VAR TYPEstart : statements\n\t\t\t| emptyempty :statements : statement ENTER next_statementnext_statement : statement ENTER next_statement\n\t\t\t\t\t| emptystatement : assignment_statement\n\t\t\t\t| declaration_statement\n\t\t\t\t| function_defination\n\t\t\t\t| for_loopassignment_statement : ID WHITESPACE EQ WHITESPACE expressiondeclaration_statement : VAR WHITESPACE ID COL WHITESPACE TYPE\n\t\t\t\t\t\t\t| VAR WHITESPACE ID COL WHITESPACE TYPE WHITESPACE EQ WHITESPACE expression\n\t\t\t\t\t\t\t| VAR WHITESPACE ID WHITESPACE EQ WHITESPACE expression expression : expression PLUS term\n\t\t\t\t| expression MINUS term\n\t\t\t\t| term\n\t\t\t\tterm : term TIMES factor\n\t\t\t| term DIVIDE factor\n\t\t\t| factor\n\tfactor : ID\n\t\t\t| NUMBER\n\tfunction_defination : FUNC WHITESPACE ID LPAREN optional_parameters RPAREN WHITESPACE optional_return_type WHITESPACE LBRACE ENTER statements RBRACEoptional_parameters : has_parameter\n\t\t\t\t\t\t| emptyhas_parameter : has_parameter COMMA has_parameter\n\t\t\t\t\t\t| ID COL WHITESPACE TYPEoptional_return_type : ARROW WHITESPACE TYPEfor_loop : FOR WHITESPACE ID WHITESPACE IN WHITESPACE NUMBER TRIPLEDOT NUMBER WHITESPACE LBRACE ENTER statements RBRACE'
    
_lr_action_items = {'COMMA':([38,60,67,],[50,50,-27,]),'MINUS':([31,32,33,34,35,54,55,56,57,58,73,],[-17,46,-21,-22,-20,-19,-18,-16,-15,46,46,]),'ID':([0,14,15,16,17,25,28,30,44,45,46,47,48,50,69,77,80,],[1,19,20,21,1,33,40,1,33,33,33,33,33,40,33,1,1,]),'TRIPLEDOT':([63,],[68,]),'VAR':([0,17,30,77,80,],[2,2,2,2,2,]),'FUNC':([0,17,30,77,80,],[3,3,3,3,3,]),'DIVIDE':([31,33,34,35,54,55,56,57,],[44,-21,-22,-20,-19,-18,44,44,]),'PLUS':([31,32,33,34,35,54,55,56,57,58,73,],[-17,47,-21,-22,-20,-19,-18,-16,-15,47,47,]),'FOR':([0,17,30,77,80,],[6,6,6,6,6,]),'WHITESPACE':([1,2,3,6,18,19,21,27,36,42,49,51,52,64,65,66,72,74,],[13,14,15,16,25,26,29,37,48,53,59,61,62,69,70,71,76,-28,]),'EQ':([13,26,59,],[18,36,64,]),'RBRACE':([17,22,24,30,43,79,82,],[-3,-4,-6,-3,-5,81,83,]),'TYPE':([37,62,70,],[49,67,74,]),'NUMBER':([25,44,45,46,47,48,53,68,69,],[34,34,34,34,34,34,63,72,34,]),'TIMES':([31,33,34,35,54,55,56,57,],[45,-21,-22,-20,-19,-18,45,45,]),'LPAREN':([20,],[28,]),'LBRACE':([71,76,],[75,78,]),'ENTER':([4,5,7,10,12,23,31,32,33,34,35,49,54,55,56,57,58,73,75,78,81,83,],[-7,-8,17,-10,-9,30,-17,-11,-21,-22,-20,-12,-19,-18,-16,-15,-14,-13,77,80,-23,-29,]),'RPAREN':([28,38,39,41,60,67,],[-3,-24,51,-25,-26,-27,]),'IN':([29,],[42,]),'$end':([0,8,9,11,17,22,24,30,43,],[-3,-2,-1,0,-3,-4,-6,-3,-5,]),'ARROW':([61,],[65,]),'COL':([19,40,],[27,52,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,17,30,77,80,],[7,23,23,7,7,]),'empty':([0,17,28,30,],[8,24,41,24,]),'statements':([0,77,80,],[9,79,82,]),'next_statement':([17,30,],[22,43,]),'expression':([25,48,69,],[32,58,73,]),'term':([25,46,47,48,69,],[31,56,57,31,31,]),'assignment_statement':([0,17,30,77,80,],[4,4,4,4,4,]),'factor':([25,44,45,46,47,48,69,],[35,54,55,35,35,35,35,]),'declaration_statement':([0,17,30,77,80,],[5,5,5,5,5,]),'has_parameter':([28,50,],[38,60,]),'optional_parameters':([28,],[39,]),'optional_return_type':([61,],[66,]),'for_loop':([0,17,30,77,80,],[10,10,10,10,10,]),'start':([0,],[11,]),'function_defination':([0,17,30,77,80,],[12,12,12,12,12,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> statements','start',1,'p_start','swift_parser.py',20),
  ('start -> empty','start',1,'p_start','swift_parser.py',21),
  ('empty -> <empty>','empty',0,'p_empty','swift_parser.py',25),
  ('statements -> statement ENTER next_statement','statements',3,'p_statements','swift_parser.py',29),
  ('next_statement -> statement ENTER next_statement','next_statement',3,'p_next_statement','swift_parser.py',33),
  ('next_statement -> empty','next_statement',1,'p_next_statement','swift_parser.py',34),
  ('statement -> assignment_statement','statement',1,'p_statement','swift_parser.py',42),
  ('statement -> declaration_statement','statement',1,'p_statement','swift_parser.py',43),
  ('statement -> function_defination','statement',1,'p_statement','swift_parser.py',44),
  ('statement -> for_loop','statement',1,'p_statement','swift_parser.py',45),
  ('assignment_statement -> ID WHITESPACE EQ WHITESPACE expression','assignment_statement',5,'p_assignment_statement','swift_parser.py',49),
  ('declaration_statement -> VAR WHITESPACE ID COL WHITESPACE TYPE','declaration_statement',6,'p_declaration_statement','swift_parser.py',60),
  ('declaration_statement -> VAR WHITESPACE ID COL WHITESPACE TYPE WHITESPACE EQ WHITESPACE expression','declaration_statement',10,'p_declaration_statement','swift_parser.py',61),
  ('declaration_statement -> VAR WHITESPACE ID WHITESPACE EQ WHITESPACE expression','declaration_statement',7,'p_declaration_statement','swift_parser.py',62),
  ('expression -> expression PLUS term','expression',3,'p_expression','swift_parser.py',88),
  ('expression -> expression MINUS term','expression',3,'p_expression','swift_parser.py',89),
  ('expression -> term','expression',1,'p_expression','swift_parser.py',90),
  ('term -> term TIMES factor','term',3,'p_term','swift_parser.py',102),
  ('term -> term DIVIDE factor','term',3,'p_term','swift_parser.py',103),
  ('term -> factor','term',1,'p_term','swift_parser.py',104),
  ('factor -> ID','factor',1,'p_factor','swift_parser.py',116),
  ('factor -> NUMBER','factor',1,'p_factor','swift_parser.py',117),
  ('function_defination -> FUNC WHITESPACE ID LPAREN optional_parameters RPAREN WHITESPACE optional_return_type WHITESPACE LBRACE ENTER statements RBRACE','function_defination',13,'p_function_defination','swift_parser.py',122),
  ('optional_parameters -> has_parameter','optional_parameters',1,'p_optional_parameters','swift_parser.py',129),
  ('optional_parameters -> empty','optional_parameters',1,'p_optional_parameters','swift_parser.py',130),
  ('has_parameter -> has_parameter COMMA has_parameter','has_parameter',3,'p_has_parameter','swift_parser.py',133),
  ('has_parameter -> ID COL WHITESPACE TYPE','has_parameter',4,'p_has_parameter','swift_parser.py',134),
  ('optional_return_type -> ARROW WHITESPACE TYPE','optional_return_type',3,'p_optional_return_type','swift_parser.py',137),
  ('for_loop -> FOR WHITESPACE ID WHITESPACE IN WHITESPACE NUMBER TRIPLEDOT NUMBER WHITESPACE LBRACE ENTER statements RBRACE','for_loop',14,'p_for_loop','swift_parser.py',140),
]
