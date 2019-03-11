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
integers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


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

def tokenize(input_file_string, output_file_path):
	current_index = 0
	ending_index = len(input_file_string)
	token_list = []

	temp_flag = False

	while current_index < ending_index:
		# Ignore spaces and newline characters when tokenizing
		if input_file_string[current_index: current_index + 1] == ' ' or \
				input_file_string[current_index: current_index + 1] == '\n' or \
				input_file_string[current_index: current_index + 1] == '\t':
			current_index += 1
		else:
			# Tokenizing keywords
			for keyword in keyword_tokens:
				if len(input_file_string[current_index:]) >= len(keyword) and input_file_string[current_index: current_index + len(keyword)] == keyword:
					current_index += len(keyword)
					token_list.append(['keyword', keyword])
					temp_flag = True
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
					temp_flag = True
					break


			# Tokenizing integerConstants
			temp_int_string = ''
			while input_file_string[current_index: current_index + 1] in integers:
				temp_int_string += input_file_string[current_index: current_index + 1]
				current_index += 1
			if temp_int_string != '':
				token_list.append(['integerConstant', temp_int_string])
			temp_int_string = ''

			# Tokenizing stringConstants
			if ending_index - current_index >= 2 and input_file_string[current_index: current_index + 1] == '\"':
				# Extract the insides of the quotes from ...x"[stringConstant]"y... where everything before x is
				# ignored using currentIndex, and everything after y is ignored.
				token_list.append(['stringConstant', input_file_string[current_index + 1: input_file_string[current_index + 1:].index('\"') + 1 + current_index]])

				# Take the length of the above and add it to the current index, +2 to account for the quotes
				current_index += len(input_file_string[current_index + 1: input_file_string[current_index + 1:].index('\"') + 1 + current_index]) + 2

			"""
			# Tokenizing identifiers
			if true:
			"""

			# Handling the cases of non-specified tokens
			if not temp_flag:
				#print('Non-Specified Token Type Found. Try to account for it in the first search?')
				current_index += 1
			else:
				temp_flag = False

	write_tokens_to_xml(token_list, output_file_path)


def write_tokens_to_xml(token_as_list, output_file_path):
	output_file = open(output_file_path, 'w')
	output_file.write('<tokens>\n')

	# Tokens in are formatted at [keyword type, data]
	for token in token_as_list:
		output_file.write('<' + token[0] + '> ' + str(token[1]) + ' </' + token[0] + '>\n')

	output_file.write('</tokens>')
	output_file.close()
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

temp_string = ''
for file_path in input_file_path_list:
	temp_string = get_file_lines_as_string(file_path)
	print(temp_string)

for file_path in output_t_file_path_list:
	tokenize(temp_string, file_path)


