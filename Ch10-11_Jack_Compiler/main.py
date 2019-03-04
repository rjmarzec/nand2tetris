import file_name_constants

#########################################
# Global Variables ######################
#########################################

# Lists of the I/O file paths. The constant name needs to be changed to adjust which file is compiled.
input_file_name_list = file_name_constants.ARRAY_TEST_IN
output_file_name_list = file_name_constants.ARRAY_TEST_OUT
output_t_file_name_list = file_name_constants.ARRAY_TEST_OUT_T


#########################################
# Cleanup and Start Functions ###########
#########################################

def get_file_lines_as_string(file_path):
	input_file = open(file_path, "r")
	result_list = input_file.readlines()
	input_file.close()

	result_string = ""
	for line in result_list:
		result_string += line

	return result_string


def other_function(variable_input):
	print('temp"')
	return


#########################################
# Element Compiler ######################
#########################################

def compile_statement():
	# if_statement | while_statement | let statement
	return


def compile_statements():
	# statement*
	return


def compile_if_statement():
	# 'if' '(' expression ')' '{' statements '}'
	return


def compile_while_statement():
	# 'if' '(' expression ')' '{' statements '}'
	return


def compile_let_statement():
	# 'let' var_name '=' expressions ';'
	return


def compile_expression():
	# term (op term)?
	return


def compile_term():
	# var_name | constant
	return


def compile_var_name():
	# a string not beginning with a digit
	return


def compile_constant():
	# a decimal number
	return


def compile_op():
	# '+' | '-' | '=' | '>' | '<'
	return


#########################################
# Testing Area ##########################
#########################################

print(file_name_constants.ARRAY_TEST_IN[0])
