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
array_test_out_xml = \
	['TestFiles/Chapter10/ArrayTestOutput/Main.xml']
array_test_out_t = \
	['TestFiles/Chapter10/ArrayTestOutput/MainT.xml']
ARRAY_TEST = [array_test_in, array_test_out_xml, array_test_out_t]

# ExpressionLessSquare
expression_less_square_in = \
	['TestFiles/Chapter10/ExpressionLessSquare/Main.jack',
		'TestFiles/Chapter10/ExpressionLessSquare/Square.jack',
		'TestFiles/Chapter10/ExpressionLessSquare/SquareGame.jack']
expression_less_square_out_xml = \
	['TestFiles/Chapter10/ExpressionLessSquareOutput/Main.xml',
		'TestFiles/Chapter10/ExpressionLessSquareOutput/Square.xml',
		'TestFiles/Chapter10/ExpressionLessSquareOutput/SquareGame.xml']
expression_less_square_out_t = \
	['TestFiles/Chapter10/ExpressionLessSquareOutput/MainT.xml',
		'TestFiles/Chapter10/ExpressionLessSquareOutput/SquareT.xml',
		'TestFiles/Chapter10/ExpressionLessSquareOutput/SquareGameT.xml']
EXPRESSION_LESS_SQUARE = [expression_less_square_in, expression_less_square_out_xml, expression_less_square_out_t]

# Square
square_in = \
	['TestFiles/Chapter10/Square/Main.jack',
		'TestFiles/Chapter10/Square/Square.jack',
		'TestFiles/Chapter10/Square/SquareGame.jack']
square_out_xml = \
	['TestFiles/Chapter10/SquareOutput/Main.xml',
		'TestFiles/Chapter10/SquareOutput/Square.xml',
		'TestFiles/Chapter10/SquareOutput/SquareGame.xml']
square_out_t = \
	['TestFiles/Chapter10/SquareOutput/MainT.xml',
		'TestFiles/Chapter10/SquareOutput/SquareT.xml',
		'TestFiles/Chapter10/SquareOutput/SquareGameT.xml']
SQUARE_10 = [square_in, square_out_xml, square_out_t]

#########################################
# Chapter 11 Files ######################
#########################################

# Average
average_in = \
	['TestFiles/Chapter11/Average/Main.jack']
average_out_xml = \
	['TestFiles/Chapter11/Average/Main.xml']
average_out_t = \
	['TestFiles/Chapter11/Average/MainT.xml']
average_out_vm = \
	['TestFiles/Chapter11/Average/Main.vm']
AVERAGE = [average_in, average_out_xml, average_out_t, average_out_vm]

# ComplexArrays
complex_arrays_in = \
	['TestFiles/Chapter11/ComplexArrays/Main.jack']
complex_arrays_out_xml = \
	['TestFiles/Chapter11/ComplexArrays/Main.xml']
complex_arrays_out_t = \
	['TestFiles/Chapter11/ComplexArrays/MainT.xml']
complex_arrays_out_vm = \
	['TestFiles/Chapter11/ComplexArrays/Main.vm']
COMPLEX_ARRAYS = [complex_arrays_in, complex_arrays_out_xml, complex_arrays_out_t, complex_arrays_out_vm]

# ConvertToBin
convert_to_bin_in = \
	['TestFiles/Chapter11/ConvertToBin/Main.jack']
convert_to_bin_out_xml = \
	['TestFiles/Chapter11/ConvertToBin/Main.xml']
convert_to_bin_out_t = \
	['TestFiles/Chapter11/ConvertToBin/MainT.xml']
convert_to_bin_out_vm = \
	['TestFiles/Chapter11/ConvertToBin/Main.vm']
CONVERT_TO_BIN = [convert_to_bin_in, convert_to_bin_out_xml, convert_to_bin_out_t, convert_to_bin_out_vm]

# Pong
pong_in = \
	['TestFiles/Chapter11/Pong/Ball.jack',
		'TestFiles/Chapter11/Pong/Bat.jack',
		'TestFiles/Chapter11/Pong/Main.jack',
		'TestFiles/Chapter11/Pong/PongGame.jack']
pong_out_xml = \
	['TestFiles/Chapter11/Pong/Ball.xml',
		'TestFiles/Chapter11/Pong/Bat.xml',
		'TestFiles/Chapter11/Pong/Main.xml',
		'TestFiles/Chapter11/Pong/PongGame.xml']
pong_out_t = \
	['TestFiles/Chapter11/Pong/BallT.xml',
		'TestFiles/Chapter11/Pong/BatT.xml',
		'TestFiles/Chapter11/Pong/MainT.xml',
		'TestFiles/Chapter11/Pong/PongGameT.xml']
pong_out_vm = \
	['TestFiles/Chapter11/Pong/Ball.vm',
		'TestFiles/Chapter11/Pong/Bat.vm',
		'TestFiles/Chapter11/Pong/Main.vm',
		'TestFiles/Chapter11/Pong/PongGame.vm']
PONG = [pong_in, pong_out_xml, pong_out_t, pong_out_vm]

# Seven
seven_in = \
	['TestFiles/Chapter11/Seven/Main.jack']
seven_out_xml = \
	['TestFiles/Chapter11/Seven/Main.xml']
seven_out_t = \
	['TestFiles/Chapter11/Seven/MainT.xml']
seven_out_vm = \
	['TestFiles/Chapter11/Seven/Main.vm']
SEVEN = [seven_in, seven_out_xml, seven_out_t, seven_out_vm]

# Square
square_in = \
	['TestFiles/Chapter11/Square/Main.jack',
		'TestFiles/Chapter11/Square/Square.jack',
		'TestFiles/Chapter11/Square/SquareGame.jack']
square_out_xml = \
	['TestFiles/Chapter11/Square/Main.xml',
		'TestFiles/Chapter11/Square/Square.xml',
		'TestFiles/Chapter11/Square/SquareGame.xml']
square_out_t = \
	['TestFiles/Chapter11/Square/MainT.xml',
		'TestFiles/Chapter11/Square/SquareT.xml',
		'TestFiles/Chapter11/Square/SquareGameT.xml']
square_out_vm = \
	['TestFiles/Chapter11/Square/Main.vm',
		'TestFiles/Chapter11/Square/Square.vm',
		'TestFiles/Chapter11/Square/SquareGame.vm']
SQUARE_11 = [square_in, square_out_xml, square_out_t, square_out_vm]
