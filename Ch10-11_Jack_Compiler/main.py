import file_name_constants
import re

#########################################
# Global Variables & Constants ##########
#########################################

# Lists of the I/O file paths. The constant name needs to be changed to adjust which file is compiled.
input_file_path_list = file_name_constants.SQUARE_IN
output_file_path_list = file_name_constants.SQUARE_OUT
output_t_file_path_list = file_name_constants.SQUARE_OUT_T


# Tokenizer Classifications
keyword_tokens = \
	['class', 'constructor', 'function', 'method', 'field', 'static', 'var', 'int', 'char', 'boolean', 'void', 'true',
		'false', 'null', 'this', 'let', 'do', 'if', 'else', 'while', 'return']
symbol_tokens = ['{', '}', '(', ')', '[', ']', '.', ',', ';', '+', '-', '*', '/', '&', '|', '<', '>', '=', '~']
integers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
spaces = [' ', '\n', '\t', '']


#########################################
# Cleanup and Start Functions ###########
#########################################

def get_file_lines_as_string(file_path):
	input_file = open(file_path, 'r')
	result_list = input_file.readlines()
	input_file.close()

	result_string = ''
	for line in result_list:
		if '//' in line:
			result_string += line[:line.index('//')]
		else:
			result_string += line

	while '/*' in result_string and '*/' in result_string:
		result_string = result_string[:result_string.index('/*')] + result_string[result_string.index('*/') + 2:]

	return result_string


#########################################
# Tokenizer Functions ###################
#########################################

def get_tokenized_input_as_string(input_file_string):
	current_index = 0
	ending_index = len(input_file_string)
	token_list = []

	while current_index < ending_index:
		token_found_this_loop = False

		# Ignore spaces and newline characters when tokenizing
		if input_file_string[current_index: current_index + 1] in spaces:
			current_index += 1
		else:
			# Tokenizing keywords
			for keyword in keyword_tokens:
				if len(input_file_string[current_index:]) >= len(keyword) and input_file_string[current_index: current_index + len(keyword)] == keyword:
					current_index += len(keyword)
					token_list.append(['keyword', keyword])
					token_found_this_loop = True
					break

			# Tokenizing symbols
			for symbol in symbol_tokens:
				if input_file_string[current_index: current_index + 1] == symbol:
					current_index += len(symbol)

					# <, >, ", and & can't be displayed normally in xml, so we handle them differently
					if symbol == '<':
						token_list.append(['symbol', '&lt;'])
					elif symbol == '>':
						token_list.append(['symbol', '&gt;'])
					elif symbol == '\"':
						token_list.append(['symbol', '&quot;'])
					elif symbol == '&':
						token_list.append(['symbol', '&amp;'])
					else:
						token_list.append(['symbol', symbol])
					token_found_this_loop = True
					break

			# Tokenizing integerConstants
			if current_index < ending_index:
				temp_int_string = ''
				while input_file_string[current_index: current_index + 1] in integers:
					temp_int_string += input_file_string[current_index: current_index + 1]
					current_index += 1
				if temp_int_string != '':
					token_list.append(['integerConstant', temp_int_string])
					token_found_this_loop = True

			# Tokenizing stringConstants
			if ending_index - current_index >= 2 and input_file_string[current_index: current_index + 1] == '\"':
				# Extract the insides of the quotes from ...x"[stringConstant]"y... where everything before x is
				# ignored using currentIndex, and everything after y is ignored.
				token_list.append(['stringConstant', input_file_string[current_index + 1: input_file_string[current_index + 1:].index('\"') + 1 + current_index]])

				# Take the length of the above and add it to the current index, +2 to account for the quotes
				current_index += len(input_file_string[current_index + 1: input_file_string[current_index + 1:].index('\"') + 1 + current_index]) + 2
				token_found_this_loop = True

			# Tokenizing identifiers
			if not token_found_this_loop:
				identifier_string = ''
				while current_index < ending_index \
					and re.match('^[A-Za-z0-9_-]*$', input_file_string[current_index: current_index + 1]):
					# This regex checks if the string is a letter, number, or underscore
					identifier_string += input_file_string[current_index: current_index + 1]
					current_index += 1
				if identifier_string != '':
					token_list.append(['identifier', identifier_string])
					token_found_this_loop = True

			# Handling the cases of non-specified tokens or strange characters
			if not token_found_this_loop:
				# print('Non-Specified Token Type Found. Try to account for it in the first search? Character:')
				# print(input_file_string[current_index:current_index + 1])
				current_index += 1

	return token_list_to_xml_string(token_list)


def token_list_to_xml_string(token_as_list):
	return_string = '<tokens>\n'

	# Tokens in are formatted at [keyword type, data]
	for token in token_as_list:
		return_string += ('<' + token[0] + '> ' + str(token[1]) + ' </' + token[0] + '>\n')

	return return_string + '</tokens>\n'


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
# Testing/Running Area ##################
#########################################

temp_string = ''

for file_path_counter in range(0, len(input_file_path_list)):
	tokenized_input_string = get_tokenized_input_as_string(get_file_lines_as_string(input_file_path_list[file_path_counter]))
	t_output_file = open(output_t_file_path_list[file_path_counter], 'w')
	t_output_file.write(tokenized_input_string)
	t_output_file.close()
