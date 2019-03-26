import file_name_constants
import re

#########################################
# Global Variables & Constants ##########
#########################################

# The program that is being compiled, as taken from file_name_constants.py
# Needs to be changed manually to change the program being compiled
program = file_name_constants.ARRAY_TEST


# Lists of the I/O file paths. Changes based on the above variable.
input_file_path_list = program[0]
output_file_path_list = program[1]
output_t_file_path_list = program[2]


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


def get_file_lines_as_list(file_path):
	input_file = open(file_path, 'r')
	result_list = input_file.readlines()
	input_file.close()

	return result_list


def get_token_value_pair_list(input_list):
	# The output is formatted as [token type, value, full line]
	result_list = []
	# Loop through all the lines of the file
	for i in range(1, len(input_list) - 1):
		pair_value = input_list[i][input_list[i].index('> ') + 2:input_list[i].index(' </')]
		pair_token = input_list[i][input_list[i].index('<') + 1:input_list[i].index('> ')]
		result_list.append([pair_token, pair_value, input_list[i]])
	return result_list


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

	return token_list_to_tokenizer_output(token_list)


def token_list_to_tokenizer_output(token_as_list):
	return_string = '<tokens>\n'

	# Token list is formatted as: [keyword type, data]
	for token in token_as_list:
		return_string += ('<' + token[0] + '> ' + str(token[1]) + ' </' + token[0] + '>\n')

	return return_string + '</tokens>\n'


#########################################
# Element Compiler ######################
#########################################
compiler_index_counter = 0
compiler_tabs = ''


# Program Structure #####################
# Note: Tokens are formatted as follows: [token type, value, full line
def compile_class(token_list_input):
	# 'class' className '{' classVarDec* subroutineDec* '}'
	global compiler_index_counter
	global compiler_tabs

	output_string = compiler_tabs + '<class>\n'
	compiler_tabs += '\t'

	output_string += compile_lexical_element(token_list_input)  # 'class'
	output_string += compile_class_name(token_list_input)  # className
	output_string += compile_lexical_element(token_list_input)  # '{'

	while token_list_input[compiler_index_counter][1] == 'static'\
		or token_list_input[compiler_index_counter][1] == 'field':
		output_string += compile_class_var_dec(token_list_input)  # classVarDec*

	while token_list_input[compiler_index_counter][1] == 'constructor'\
		or token_list_input[compiler_index_counter][1] == 'function'\
		or token_list_input[compiler_index_counter][1] == 'method':
		output_string += compile_subroutine_dec(token_list_input)  # subroutineDec*

	output_string += compile_lexical_element(token_list_input)  # '}'

	compiler_tabs = compiler_tabs.replace('\t', '', 1)
	output_string += '</class>\n'
	return output_string


def compile_class_var_dec(token_list_input):
	# ('static'|'field') type varName* (',' varName)* ';'
	global compiler_index_counter
	global compiler_tabs

	output_string = compiler_tabs + '<classVarDec>\n'

	output_string += compile_lexical_element(token_list_input)  # ('static'|'field')
	output_string += compile_type(token_list_input)  # type

	while token_list_input[compiler_index_counter][0] == 'identifier':
		output_string += compile_var_name(token_list_input)  # varName*

	while token_list_input[compiler_index_counter][1] == ',':
		output_string += compile_lexical_element(token_list_input)  # (',' ...
		output_string += compile_var_name(token_list_input)  # ...varName)*

	output_string += compile_lexical_element(token_list_input)  # ';'

	return output_string + compiler_tabs + '</classVarDec>\n'


def compile_type(token_list_input):
	# 'int'|'char'|'boolean'|className
	global compiler_index_counter
	global compiler_tabs

	if token_list_input[compiler_index_counter][1] == 'int'\
		or token_list_input[compiler_index_counter][1] == 'char' \
		or token_list_input[compiler_index_counter][1] == 'bool':
		output_string = compile_lexical_element(token_list_input)  # 'int'|'char'|'boolean'|...
	else:
		output_string = compile_class_name(token_list_input)  # ...|className

	return output_string


def compile_subroutine_dec(token_list_input):
	# ('constructor'|'function'|'method') ('void'|type) subroutineName '(' parameterList ')' subroutineBody
	global compiler_index_counter
	global compiler_tabs

	output_string = compile_lexical_element(token_list_input)  # ('constructor'|'function'|'method')

	if token_list_input[compiler_index_counter][1] == 'void':
		output_string += compile_lexical_element(token_list_input)  # ('void'|...
	else:
		output_string += compile_type(token_list_input)  # ...|type)

	output_string += compile_subroutine_name(token_list_input)  # subroutineName
	output_string += compile_lexical_element(token_list_input)  # '('
	output_string += compile_parameter_list(token_list_input)  # parameterList
	output_string += compile_lexical_element(token_list_input)  # ')'
	output_string += compile_subroutine_body(token_list_input)  # subroutineBody

	compiler_index_counter += 1
	return output_string


def compile_parameter_list(token_list_input):
	# ((type varName) (',' type varName)*)?
	global compiler_index_counter
	global compiler_tabs

	output_string = ''

	# Checking to see if the next token is a type manually
	if token_list_input[compiler_index_counter][1] == 'int'\
		or token_list_input[compiler_index_counter][1] == 'char' \
		or token_list_input[compiler_index_counter][1] == 'bool':  # (...)?
		output_string += compile_type(token_list_input)  # (type ...
		output_string += compile_var_name(token_list_input)  # ... varName)

	while token_list_input[compiler_index_counter][1] == ',':
		output_string += compile_lexical_element(token_list_input)  # ','
		output_string += compile_type(token_list_input)  # type
		output_string += compile_var_name(token_list_input)  # varName

	return output_string


def compile_subroutine_body(token_list_input):
	# '{' varDec* statements '}'
	global compiler_index_counter
	global compiler_tabs

	output_string = compile_lexical_element(token_list_input)  # '{'

	while token_list_input[compiler_index_counter][1] == 'var':
		output_string += compile_var_dec(token_list_input)  # varDec*

	output_string += compile_statements(token_list_input)  # statements
	output_string += compile_lexical_element(token_list_input)  # '}'

	return output_string


def compile_var_dec(token_list_input):
	# 'var' type varName (',' type varName)* ';'
	global compiler_index_counter
	global compiler_tabs

	output_string = compile_lexical_element(token_list_input)  # 'var'
	output_string += compile_type(token_list_input)  # type
	output_string += compile_var_name(token_list_input)  # varName

	while token_list_input[compiler_index_counter][1] == ',':  # (...)*
		output_string += compile_lexical_element(token_list_input)  # ','
		output_string += compile_type(token_list_input)  # type
		output_string += compile_var_name(token_list_input)  # varName

	output_string += compile_lexical_element(token_list_input)  # ';'

	return output_string


def compile_class_name(token_list_input):
	# identifier
	global compiler_index_counter
	global compiler_tabs

	compiler_index_counter += 1
	return compiler_tabs + token_list_input[compiler_index_counter - 1][2]


def compile_subroutine_name(token_list_input):
	# identifier
	global compiler_index_counter
	global compiler_tabs

	compiler_index_counter += 1
	return compiler_tabs + token_list_input[compiler_index_counter - 1][2]


def compile_var_name(token_list_input):
	# identifier
	global compiler_index_counter
	global compiler_tabs

	compiler_index_counter += 1
	return compiler_tabs + token_list_input[compiler_index_counter - 1][2]


# Statements ############################
def compile_statements(token_list_input):
	# TODO: Complete this method
	# statement*
	global compiler_index_counter
	global compiler_tabs

	return ''


def compile_statement(token_list_input):
	# TODO: Complete this method
	# letStatement|ifStatement|whileStatement|doStatement|returnStatement
	global compiler_index_counter
	global compiler_tabs

	return ''


def compile_let_statement(token_list_input):
	# TODO: Complete this method
	# 'let' varName ('[' expression ']')? '=' expression ';'
	global compiler_index_counter
	global compiler_tabs

	return ''


def compile_if_statement(token_list_input):
	# TODO: Complete this method
	# 'if' '(' expression ('[' expression ']')? '=' expression ';'
	global compiler_index_counter
	global compiler_tabs

	return ''


def compile_while_statement(token_list_input):
	# TODO: Complete this method
	# 'while' '(' expression ')' '{' statements '}' 'else' '{' statements '}' )?
	global compiler_index_counter
	global compiler_tabs

	return ''


def compile_do_statement(token_list_input):
	# TODO: Complete this method
	# 'do' subroutineCall ';'
	global compiler_index_counter
	global compiler_tabs

	return ''


def compile_return_statement(token_list_input):
	# TODO: Complete this method
	# 'return' expression? ';'
	global compiler_index_counter
	global compiler_tabs

	return ''


# Expressions ###########################
def compile_expression(token_list_input):
	# TODO: Complete this method
	# term (op term)*
	global compiler_index_counter
	global compiler_tabs

	return ''


def compile_term(token_list_input):
	# TODO: Complete this method
	# integerConstant | stringConstant | keywordConstant | varName | varName '[' expression ']' | subroutineCall |
	# '(' expression ')' | unaryOp term
	global compiler_index_counter
	global compiler_tabs

	return ''


def compile_subroutine_call(token_list_input):
	# TODO: Complete this method
	# subroutineName '(' expressionList ')' | (className | varName) '.' subroutineName '(' expressionList ')'
	global compiler_index_counter
	global compiler_tabs

	return ''


def compile_expressions(token_list_input):
	# TODO: Complete this method
	# (expression (',' expression)* )?
	global compiler_index_counter
	global compiler_tabs

	return ''


def compile_op(token_list_input):
	# TODO: Complete this method
	# '+' | '-' | '*' | '/' | '&' | '|' | '<' | '>' | '='
	global compiler_index_counter
	global compiler_tabs

	return ''


def compile_unary_op(token_list_input):
	# TODO: Complete this method
	# '-' | '~'
	global compiler_index_counter
	global compiler_tabs

	return ''


def compile_keyword_constant(token_list_input):
	# TODO: Complete this method
	# 'true' | 'false' | 'null' | 'this'
	global compiler_index_counter
	global compiler_tabs

	return ''


# Lexical elements
def compile_lexical_element(token_list_input):
	# keyword | symbol | integerConstant | StringConstant | identifier
	global compiler_index_counter
	global compiler_tabs

	compiler_index_counter += 1
	return compiler_tabs + token_list_input[compiler_index_counter - 1][2]


#########################################
# Testing/Running Area ##################
#########################################

temp_string = ''

# Tokenize the Input File
for file_path_counter in range(0, len(input_file_path_list)):
	tokenized_input_string = get_tokenized_input_as_string(get_file_lines_as_string(input_file_path_list[file_path_counter]))

	t_output_file = open(output_t_file_path_list[file_path_counter], 'w')
	t_output_file.write(tokenized_input_string)
	t_output_file.close()

# Syntax Analysis of the Tokenized Input
for file_path_counter in range(0, len(output_t_file_path_list)):
	tokenized_input_string = get_file_lines_as_list(output_t_file_path_list[file_path_counter])
	syntax_analyzer_output = compile_class(get_token_value_pair_list(tokenized_input_string))

	syntax_analyzer_output_file = open(output_file_path_list[file_path_counter], 'w')
	syntax_analyzer_output_file.write(syntax_analyzer_output)
	syntax_analyzer_output_file.close()


# print(get_token_value_pair_list(get_file_lines_as_list(output_t_file_path_list[0])))
