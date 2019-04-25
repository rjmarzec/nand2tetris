# A file containing constants of the project file names so that it is easier to switch between them when testing

#########################################
# Template ##############################
#########################################

# Files Name ####################
# ..._in = ['TestFiles/Chapter.../.../....jack', '...']	(Input File Directory as a List)
# ..._out = ['.../.../....vm', '...']	(Output File Directory as a List)
# ..._out_t = ['.../.../....vm', '...']	(Tokenizer Output File Directory as a List)
# ... = [..._in, ..._out, ..._out_t] (A public collection of the above as a list, in the order shown above)

#########################################
# Chapter 10 Files #######################
#########################################

# ArrayTest
array_test_in = \
	['TestFiles/Chapter10/ArrayTest/Main.jack']
array_test_out = \
	['TestFiles/Chapter10/ArrayTestOutput/Main.xml']
array_test_out_t = \
	['TestFiles/Chapter10/ArrayTestOutput/MainT.xml']
ARRAY_TEST = [array_test_in, array_test_out, array_test_out_t]

# ExpressionLessSquare
expression_less_square_in = \
	['TestFiles/Chapter10/ExpressionLessSquare/Main.jack',
		'TestFiles/Chapter10/ExpressionLessSquare/Square.jack',
		'TestFiles/Chapter10/ExpressionLessSquare/SquareGame.jack']
expression_less_square_out = \
	['TestFiles/Chapter10/ExpressionLessSquareOutput/Main.xml',
		'TestFiles/Chapter10/ExpressionLessSquareOutput/Square.xml',
		'TestFiles/Chapter10/ExpressionLessSquareOutput/SquareGame.xml']
expression_less_square_out_t = \
	['TestFiles/Chapter10/ExpressionLessSquareOutput/MainT.xml',
		'TestFiles/Chapter10/ExpressionLessSquareOutput/SquareT.xml',
		'TestFiles/Chapter10/ExpressionLessSquareOutput/SquareGameT.xml']
EXPRESSION_LESS_SQUARE = [expression_less_square_in, expression_less_square_out, expression_less_square_out_t]

# Square
square_in = \
	['TestFiles/Chapter10/Square/Main.jack',
		'TestFiles/Chapter10/Square/Square.jack',
		'TestFiles/Chapter10/Square/SquareGame.jack']
square_out = \
	['TestFiles/Chapter10/SquareOutput/Main.xml',
		'TestFiles/Chapter10/SquareOutput/Square.xml',
		'TestFiles/Chapter10/SquareOutput/SquareGame.xml']
square_out_t = \
	['TestFiles/Chapter10/SquareOutput/MainT.xml',
		'TestFiles/Chapter10/SquareOutput/SquareT.xml',
		'TestFiles/Chapter10/SquareOutput/SquareGameT.xml']
SQUARE = [square_in, square_out, square_out_t]

#########################################
# Chapter 10 Files ######################
#########################################

# ...
