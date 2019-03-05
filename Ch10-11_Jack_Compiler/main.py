import file_name_constants

#########################################
# Global Variables & Constants ##########
#########################################

# Lists of the I/O file paths. The constant name needs to be changed to adjust which file is compiled.
input_file_path_list = file_name_constants.ARRAY_TEST_IN
output_file_path_list = file_name_constants.ARRAY_TEST_OUT
output_t_file_path_list = file_name_constants.ARRAY_TEST_OUT_T


# Tokenizer Classifications
keyword_tokens = \
	['class', 'constructor', 'function', 'method', 'field', 'static', 'var', 'int', 'char', 'boolean', 'void', 'true',
		'if', 'else', 'while', 'return']
symbol_tokens = ['{', '}', '(', ')', '[', ']', '.', ',', ';', '+', '-', '*', '/', '&', '|', '<', '>', '=', '~']


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


#########################################
# Tokenizer Functions ###################
#########################################

def tokenize(input_file_string, output_file_path):
	current_index = 0
	ending_index = len(input_file_string)
	token_list = []

	while current_index < ending_index:
		if input_file_string[current_index, current_index + 1] == ' ' or \
				input_file_string[current_index, current_index + 1] == '\n':
			current_index += 1
		else:
			for keyword in keyword_tokens:
				if input_file_string[current_index, current_index + len(keyword)] == keyword:
					current_index += len(keyword)
					token_list.append(['keyword', keyword])


def write_tokens_to_xml(token_as_list, output_file_path):
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

print(file_name_constants.ARRAY_TEST_IN[0] + "\n")

for file_path in input_file_path_list:
	temp_string = get_file_lines_as_string(file_path)
	print(temp_string)

	# tokenize(temp_string)


