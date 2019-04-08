# A file containing constants of the project file names so that it is easier to switch between them when testing

#########################################
# Template ##############################
#########################################

# Files Name ####################
# ..._IN = ['TestFiles/Chapter.../.../....jack', '...']	(Input File Directory as a List)
# ..._OUT = ['.../.../....vm', '...']	(Output File Directory as a List)
# ..._OUT_T = ['.../.../....vm', '...']	(Tokenizer Output File Directory as a List)
# ... = [..._IN, ..._OUT, ..._OUT_T] (A collection of the above as a list, in the order shown above)

#########################################
# Chapter 9 Files #######################
#########################################

# ArrayTest
ARRAY_TEST_IN = \
	['TestFiles/Chapter10/ArrayTest/Main.jack']
ARRAY_TEST_OUT = \
	['TestFiles/Chapter10/ArrayTestOutput/Main.xml']
ARRAY_TEST_OUT_T = \
	['TestFiles/Chapter10/ArrayTestOutput/MainT.xml']
ARRAY_TEST = [ARRAY_TEST_IN, ARRAY_TEST_OUT, ARRAY_TEST_OUT_T]

# ExpressionLessSquare
EXPRESSION_LESS_SQUARE_IN = \
	['TestFiles/Chapter10/ExpressionLessSquare/Main.jack',
		'TestFiles/Chapter10/ExpressionLessSquare/Square.jack',
		'TestFiles/Chapter10/ExpressionLessSquare/SquareGame.jack']
EXPRESSION_LESS_SQUARE_OUT = \
	['TestFiles/Chapter10/ExpressionLessSquareOutput/Main.xml',
		'TestFiles/Chapter10/ExpressionLessSquareOutput/Square.xml',
		'TestFiles/Chapter10/ExpressionLessSquareOutput/SquareGame.xml']
EXPRESSION_LESS_SQUARE_OUT_T = \
	['TestFiles/Chapter10/ExpressionLessSquareOutput/MainT.xml',
		'TestFiles/Chapter10/ExpressionLessSquareOutput/SquareT.xml',
		'TestFiles/Chapter10/ExpressionLessSquareOutput/SquareGameT.xml']
EXPRESSION_LESS_SQUARE = [EXPRESSION_LESS_SQUARE_IN, EXPRESSION_LESS_SQUARE_OUT, EXPRESSION_LESS_SQUARE_OUT_T]

# Square
SQUARE_IN = \
	['TestFiles/Chapter10/Square/Main.jack',
		'TestFiles/Chapter10/Square/Square.jack',
		'TestFiles/Chapter10/Square/SquareGame.jack']
SQUARE_OUT = \
	['TestFiles/Chapter10/SquareOutput/Main.xml',
		'TestFiles/Chapter10/SquareOutput/Square.xml',
		'TestFiles/Chapter10/SquareOutput/SquareGame.xml']
SQUARE_OUT_T = \
	['TestFiles/Chapter10/SquareOutput/MainT.xml',
		'TestFiles/Chapter10/SquareOutput/SquareT.xml',
		'TestFiles/Chapter10/SquareOutput/SquareGameT.xml']
SQUARE = [SQUARE_IN, SQUARE_OUT, SQUARE_OUT_T]

#########################################
# Chapter 10 Files ######################
#########################################

# ...
