import file_name_constants
import re

#########################################
# Global Variables & Constants ##########
#########################################

# The program that is being compiled, as taken from file_name_constants.py
# Needs to be changed manually to change the program being compiled
program = file_name_constants.SEVEN


# Lists of the I/O file paths. Changes based on the above variable.
input_file_path_list = program[0]
output_file_path_list = program[1]
output_t_file_path_list = program[2]
output_vm_file_path_list = program[3]


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
				if len(input_file_string[current_index:]) >= len(keyword) \
					and input_file_string[current_index: current_index + len(keyword)] == keyword:
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
vm_output = ''
compiler_index_counter = 0
compiler_tabs = ''


# Program Structure #####################
# Note: Tokens are formatted as follows: [token type, value, full line
def compile_class(token_list_input):
	# 'class' className '{' classVarDec* subroutineDec* '}'
	global compiler_index_counter
	global compiler_tabs
	global vm_output
	

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

	compiler_index_counter = 0
	compiler_tabs = ''
	return output_string.replace('\t', '  ')


def compile_class_var_dec(token_list_input):
	# ('static'|'field') type varName* (',' varName)* ';'
	global compiler_index_counter
	global compiler_tabs
	global vm_output

	output_string = compiler_tabs + '<classVarDec>\n'
	compiler_tabs += '\t'

	output_string += compile_lexical_element(token_list_input)  # ('static'|'field')
	output_string += compile_type(token_list_input)  # type

	while token_list_input[compiler_index_counter][0] == 'identifier':
		output_string += compile_var_name(token_list_input)  # varName*

	while token_list_input[compiler_index_counter][1] == ',':
		output_string += compile_lexical_element(token_list_input)  # (',' ...
		output_string += compile_var_name(token_list_input)  # ...varName)*

	output_string += compile_lexical_element(token_list_input)  # ';'

	compiler_tabs = compiler_tabs.replace('\t', '', 1)
	return output_string + compiler_tabs + '</classVarDec>\n'


def compile_type(token_list_input):
	# 'int'|'char'|'boolean'|className
	global compiler_index_counter
	global compiler_tabs
	global vm_output

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
	global vm_output

	output_string = compiler_tabs + '<subroutineDec>\n'
	compiler_tabs += '\t'

	output_string += compile_lexical_element(token_list_input)  # ('constructor'|'function'|'method')

	if token_list_input[compiler_index_counter][1] == 'void':
		output_string += compile_lexical_element(token_list_input)  # ('void'|...
	else:
		output_string += compile_type(token_list_input)  # ...|type)

	output_string += compile_subroutine_name(token_list_input)  # subroutineName
	output_string += compile_lexical_element(token_list_input)  # '('
	output_string += compile_parameter_list(token_list_input)  # parameterList
	output_string += compile_lexical_element(token_list_input)  # ')'
	output_string += compile_subroutine_body(token_list_input)  # subroutineBody

	compiler_tabs = compiler_tabs.replace('\t', '', 1)
	output_string += compiler_tabs + '</subroutineDec>\n'
	return output_string


def compile_parameter_list(token_list_input):
	# ((type varName) (',' type varName)*)?
	global compiler_index_counter
	global compiler_tabs
	global vm_output

	output_string = compiler_tabs + '<parameterList>\n'
	compiler_tabs += '\t'

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

	compiler_tabs = compiler_tabs.replace('\t', '', 1)
	output_string += compiler_tabs + '</parameterList>\n'
	return output_string


def compile_subroutine_body(token_list_input):
	# '{' varDec* statements '}'
	global compiler_index_counter
	global compiler_tabs
	global vm_output

	output_string = compiler_tabs + '<subroutineBody>\n'
	compiler_tabs += '\t'

	output_string += compile_lexical_element(token_list_input)  # '{'

	while token_list_input[compiler_index_counter][1] == 'var':
		output_string += compile_var_dec(token_list_input)  # varDec*

	output_string += compile_statements(token_list_input)  # statements
	output_string += compile_lexical_element(token_list_input)  # '}'

	compiler_tabs = compiler_tabs.replace('\t', '', 1)

	output_string += compiler_tabs + '</subroutineBody>\n'
	return output_string


def compile_var_dec(token_list_input):
	# 'var' type varName (',' varName)* ';'
	global compiler_index_counter
	global compiler_tabs
	global vm_output

	output_string = compiler_tabs + '<varDec>\n'
	compiler_tabs += '\t'

	output_string += compile_lexical_element(token_list_input)  # 'var'
	output_string += compile_type(token_list_input)  # type
	output_string += compile_var_name(token_list_input)  # varName

	while token_list_input[compiler_index_counter][1] == ',':  # (...)*
		output_string += compile_lexical_element(token_list_input)  # ','
		output_string += compile_var_name(token_list_input)  # varName

	output_string += compile_lexical_element(token_list_input)  # ';'

	compiler_tabs = compiler_tabs.replace('\t', '', 1)
	output_string += compiler_tabs + '</varDec>\n'
	return output_string


def compile_class_name(token_list_input):
	# identifier
	global compiler_index_counter
	global compiler_tabs
	global vm_output

	return compile_lexical_element(token_list_input)


def compile_subroutine_name(token_list_input):
	# identifier
	global compiler_index_counter
	global compiler_tabs
	global vm_output

	return compile_lexical_element(token_list_input)


def compile_var_name(token_list_input):
	# identifier
	global compiler_index_counter
	global compiler_tabs
	global vm_output

	return compile_lexical_element(token_list_input)


# Statements ############################

def compile_statements(token_list_input):
	# statement*
	global compiler_index_counter
	global compiler_tabs
	global vm_output

	output_string = compiler_tabs + '<statements>\n'
	compiler_tabs += '\t'

	while token_list_input[compiler_index_counter][1] == 'let'\
		or token_list_input[compiler_index_counter][1] == 'if'\
		or token_list_input[compiler_index_counter][1] == 'while'\
		or token_list_input[compiler_index_counter][1] == 'do'\
		or token_list_input[compiler_index_counter][1] == 'return':
		output_string += compile_statement(token_list_input)  # statement*

	compiler_tabs = compiler_tabs.replace('\t', '', 1)
	output_string += compiler_tabs + '</statements>\n'
	return output_string


def compile_statement(token_list_input):
	# letStatement|ifStatement|whileStatement|doStatement|returnStatement
	global compiler_index_counter
	global compiler_tabs
	global vm_output

	if token_list_input[compiler_index_counter][1] == 'let':
		output_string = compile_let_statement(token_list_input)  # letStatement|...
	elif token_list_input[compiler_index_counter][1] == 'if':
		output_string = compile_if_statement(token_list_input)  # ...|ifStatement|...
	elif token_list_input[compiler_index_counter][1] == 'while':
		output_string = compile_while_statement(token_list_input)  # ...|whileStatement|...
	elif token_list_input[compiler_index_counter][1] == 'do':
		output_string = compile_do_statement(token_list_input)  # ...|doStatement|...
	else:
		output_string = compile_return_statement(token_list_input)  # ...|returnStatement

	return output_string


def compile_let_statement(token_list_input):
	# 'let' varName ('[' expression ']')? '=' expression ';'
	global compiler_index_counter
	global compiler_tabs
	global vm_output

	output_string = compiler_tabs + '<letStatement>\n'
	compiler_tabs += '\t'

	output_string += compile_lexical_element(token_list_input)  # 'let'
	output_string += compile_var_name(token_list_input)  # varName

	if token_list_input[compiler_index_counter][1] == '[':  # (...)?
		output_string += compile_lexical_element(token_list_input)  # '['
		output_string += compile_expression(token_list_input)  # expression
		output_string += compile_lexical_element(token_list_input)  # ']'

	output_string += compile_lexical_element(token_list_input)  # '='
	output_string += compile_expression(token_list_input)   # expression
	output_string += compile_lexical_element(token_list_input)  # ';'

	compiler_tabs = compiler_tabs.replace('\t', '', 1)
	output_string += compiler_tabs + '</letStatement>\n'
	return output_string


def compile_if_statement(token_list_input):
	# 'if' '(' expression ')' '{' statements '}' ('else' '{' statements '}')?
	global compiler_index_counter
	global compiler_tabs
	global vm_output

	output_string = compiler_tabs + '<ifStatement>\n'
	compiler_tabs += '\t'

	output_string += compile_lexical_element(token_list_input)  # 'if'
	output_string += compile_lexical_element(token_list_input)  # '('
	output_string += compile_expression(token_list_input)  # expression
	output_string += compile_lexical_element(token_list_input)  # ')'

	output_string += compile_lexical_element(token_list_input)  # '{'
	output_string += compile_statements(token_list_input)  # statements
	output_string += compile_lexical_element(token_list_input)  # '}'

	if token_list_input[compiler_index_counter][1] == 'else':  # (...)?
		output_string += compile_lexical_element(token_list_input)  # 'else'
		output_string += compile_lexical_element(token_list_input)  # '{'
		output_string += compile_statements(token_list_input)  # statements
		output_string += compile_lexical_element(token_list_input)  # '}'

	compiler_tabs = compiler_tabs.replace('\t', '', 1)
	output_string += compiler_tabs + '</ifStatement>\n'
	return output_string


def compile_while_statement(token_list_input):
	# 'while' '(' expression ')' '{' statements '}'
	global compiler_index_counter
	global compiler_tabs
	global vm_output

	output_string = compiler_tabs + '<whileStatement>\n'
	compiler_tabs += '\t'

	output_string += compile_lexical_element(token_list_input)  # 'while'
	output_string += compile_lexical_element(token_list_input)  # '('
	output_string += compile_expression(token_list_input)  # expression
	output_string += compile_lexical_element(token_list_input)  # ')'
	output_string += compile_lexical_element(token_list_input)  # '{'
	output_string += compile_statements(token_list_input)  # statements
	output_string += compile_lexical_element(token_list_input)  # '}'

	compiler_tabs = compiler_tabs.replace('\t', '', 1)
	output_string += compiler_tabs + '</whileStatement>\n'
	return output_string


def compile_do_statement(token_list_input):
	# 'do' subroutineCall ';'
	global compiler_index_counter
	global compiler_tabs
	global vm_output

	output_string = compiler_tabs + '<doStatement>\n'
	compiler_tabs += '\t'

	output_string += compile_lexical_element(token_list_input)  # 'do'
	output_string += compile_subroutine_call(token_list_input)  # subroutineCall
	output_string += compile_lexical_element(token_list_input)  # ';'

	compiler_tabs = compiler_tabs.replace('\t', '', 1)
	output_string += compiler_tabs + '</doStatement>\n'
	return output_string


def compile_return_statement(token_list_input):
	# 'return' expression? ';'
	global compiler_index_counter
	global compiler_tabs
	global vm_output

	output_string = compiler_tabs + '<returnStatement>\n'
	compiler_tabs += '\t'

	output_string += compile_lexical_element(token_list_input)  # 'return'

	if token_list_input[compiler_index_counter][1] != ';':  # expression?
		output_string += compile_expression(token_list_input)  # expression

	output_string += compile_lexical_element(token_list_input)  # ';'

	compiler_tabs = compiler_tabs.replace('\t', '', 1)
	output_string += compiler_tabs + '</returnStatement>\n'
	return output_string


# Expressions ###########################

def compile_expression(token_list_input):
	# term (op term)*
	global compiler_index_counter
	global compiler_tabs
	global vm_output

	output_string = compiler_tabs + '<expression>\n'
	compiler_tabs += '\t'

	output_string += compile_term(token_list_input)  # term

	while token_list_input[compiler_index_counter][1] == '+'\
		or token_list_input[compiler_index_counter][1] == '-' \
		or token_list_input[compiler_index_counter][1] == '*' \
		or token_list_input[compiler_index_counter][1] == '/' \
		or token_list_input[compiler_index_counter][1] == '&amp;' \
		or token_list_input[compiler_index_counter][1] == '&' \
		or token_list_input[compiler_index_counter][1] == '|' \
		or token_list_input[compiler_index_counter][1] == '&lt;' \
		or token_list_input[compiler_index_counter][1] == '<' \
		or token_list_input[compiler_index_counter][1] == '&gt;' \
		or token_list_input[compiler_index_counter][1] == '>' \
		or token_list_input[compiler_index_counter][1] == '=':  # (...)*
		output_string += compile_lexical_element(token_list_input)  # op
		output_string += compile_term(token_list_input)  # term

	compiler_tabs = compiler_tabs.replace('\t', '', 1)
	output_string += compiler_tabs + '</expression>\n'
	return output_string


def compile_term(token_list_input):
	# integerConstant | stringConstant | keywordConstant | varName | varName '[' expression ']' | subroutineCall |
	# '(' expression ')' | unaryOp term
	global compiler_index_counter
	global compiler_tabs
	global vm_output

	output_string = compiler_tabs + '<term>\n'
	compiler_tabs += '\t'

	# integerConstant | ...
	if token_list_input[compiler_index_counter][0] == 'integerConstant':
		output_string += compile_lexical_element(token_list_input)

	# ... | stringConstant | ...
	elif token_list_input[compiler_index_counter][0] == 'stringConstant':
		output_string += compile_lexical_element(token_list_input)

	# ... | keywordConstant | ...
	elif token_list_input[compiler_index_counter][0] == 'keywordConstant'\
		or token_list_input[compiler_index_counter][0] == 'keyword':
		output_string += compile_lexical_element(token_list_input)

	# ... | varName ('[' expression ']')? | subroutineCall | ...
	# varName and subroutineCall both start with an identifier, so we have to figure out which on it is
	elif token_list_input[compiler_index_counter][0] == 'identifier':
		if token_list_input[compiler_index_counter + 1][1] == '('\
			or token_list_input[compiler_index_counter + 1][1] == '.':
			output_string += compile_subroutine_call(token_list_input)  # subroutineCall
		else:
			output_string += compile_lexical_element(token_list_input)  # varName
			if token_list_input[compiler_index_counter][1] == '[':  # (...)?
				output_string += compile_lexical_element(token_list_input)  # '['
				output_string += compile_expression(token_list_input)  # expression
				output_string += compile_lexical_element(token_list_input)  # ']'

	# ... | '(' expression ')' | ...
	elif token_list_input[compiler_index_counter][1] == '(':
		output_string += compile_lexical_element(token_list_input)  # '('
		output_string += compile_expression(token_list_input)  # expression
		output_string += compile_lexical_element(token_list_input)  # ')'

	# ... | unaryOp term
	elif token_list_input[compiler_index_counter][1] == '-'\
		or token_list_input[compiler_index_counter][1] == '~':
		output_string += compile_unary_op(token_list_input)  # unaryOp
		output_string += compile_term(token_list_input)  # term

	compiler_tabs = compiler_tabs.replace('\t', '', 1)
	output_string += compiler_tabs + '</term>\n'
	return output_string


def compile_subroutine_call(token_list_input):
	# subroutineName '(' expressionList ')' | (className | varName) '.' subroutineName '(' expressionList ')'
	# which can be simplified to:
	# ((className | varName) '.')? subroutineName '(' expressionList ')'
	global compiler_index_counter
	global compiler_tabs
	global vm_output

	# output_string = compiler_tabs + '<subroutineCall>\n'
	# compiler_tabs += '\t'
	output_string = ''

	if token_list_input[compiler_index_counter + 1][1] == '.':  # (...)?
		# className and varName ultimately give the same output, so we don't care which one it really is
		output_string += compile_class_name(token_list_input)  # (className | varName)
		output_string += compile_lexical_element(token_list_input)  # '.'

	output_string += compile_subroutine_name(token_list_input)  # subroutineName
	output_string += compile_lexical_element(token_list_input)  # '('
	output_string += compile_expression_list(token_list_input)  # expressionList
	output_string += compile_lexical_element(token_list_input)  # ')'

	# compiler_tabs = compiler_tabs.replace('\t', '', 1)
	# output_string += compiler_tabs + '</subroutineCall>\n'
	return output_string


def compile_expression_list(token_list_input):
	# (expression (',' expression)* )?
	global compiler_index_counter
	global compiler_tabs
	global vm_output

	output_string = compiler_tabs + '<expressionList>\n'
	compiler_tabs += '\t'

	if token_list_input[compiler_index_counter][0] == 'integerConstant'\
		or token_list_input[compiler_index_counter][0] == 'stringConstant'\
		or token_list_input[compiler_index_counter][0] == 'keywordConstant' \
		or token_list_input[compiler_index_counter][0] == 'keyword' \
		or token_list_input[compiler_index_counter][0] == 'identifier'\
		or token_list_input[compiler_index_counter][1] == '('\
		or token_list_input[compiler_index_counter][1] == '-' \
		or token_list_input[compiler_index_counter][1] == '~':  # (...)?
		output_string += compile_expression(token_list_input)  # expression

		while token_list_input[compiler_index_counter][1] == ',':  # (...)*
			output_string += compile_lexical_element(token_list_input)  # ','
			output_string += compile_expression(token_list_input)  # expression

	compiler_tabs = compiler_tabs.replace('\t', '', 1)
	output_string += compiler_tabs + '</expressionList>\n'
	return output_string


def compile_op(token_list_input):
	# '+' | '-' | '*' | '/' | '&' | '|' | '<' | '>' | '='
	global compiler_index_counter
	global compiler_tabs
	global vm_output

	output_string = compiler_tabs + '<op>\n'
	compiler_tabs += '\t'

	output_string += compile_lexical_element(token_list_input)  # '+' | '-' | '*' | '/' | '&' | '|' | '<' | '>' | '='

	compiler_tabs = compiler_tabs.replace('\t', '', 1)
	output_string += compiler_tabs + '</op>\n'
	return output_string


def compile_unary_op(token_list_input):
	# '-' | '~'
	global compiler_index_counter
	global compiler_tabs
	global vm_output

	output_string = compile_lexical_element(token_list_input)  # '-' | '~'

	return output_string


def compile_keyword_constant(token_list_input):
	# 'true' | 'false' | 'null' | 'this'
	global compiler_index_counter
	global compiler_tabs
	global vm_output

	output_string = compiler_tabs + '<keywordConstant>\n'
	compiler_tabs += '\t'

	output_string += compile_lexical_element(token_list_input)  # 'true' | 'false' | 'null' | 'this'

	compiler_tabs = compiler_tabs.replace('\t', '', 1)
	output_string += compiler_tabs + '</keywordConstant>\n'
	return output_string


# Lexical elements
def compile_lexical_element(token_list_input):
	# keyword | symbol | integerConstant | StringConstant | identifier
	global compiler_index_counter
	global compiler_tabs
	global vm_output

	compiler_index_counter += 1
	return compiler_tabs + token_list_input[compiler_index_counter - 1][2]


#########################################
# VM Translator #########################
#########################################

# Used to determine in what scope variables exist
scope_stack = []


# Symbol Table Builder ##################
# name => (String)
# type => (String)
# kind => (STATIC, FIELD, ARG, or VAR)

# The static and field symbol tables are wiped per-class
static_symbol_table = {}
field_symbol_table = {}

# The argument and var symbol tables are wiped per-method/function/constructor
argument_symbol_table = {}
var_symbol_table = {}


def reset_symbol_table():
	# resets the entire symbol table
	global static_symbol_table
	global field_symbol_table

	static_symbol_table = {}
	field_symbol_table = {}

	start_subroutine()

	return  # void


def start_subroutine():
	# starts a new subroutine scope
	# (i.e., resets the subroutine's symbol table)
	global argument_symbol_table
	global var_symbol_table

	argument_symbol_table = []
	var_symbol_table = []

	return  # void


def define(name, type, kind):
	# defines a new identifier of a given name, type and kind and assigns it a running index.
	# STATIC and FIELD identifiers have a class scope, while ARG and VAR identifiers have a subroutine scope
	global static_symbol_table
	global field_symbol_table
	global argument_symbol_table
	global var_symbol_table

	if kind == 'STATIC':
		static_symbol_table.update({name: type})
	elif kind == 'FIELD':
		field_symbol_table.update({name: type})
	elif kind == 'ARG':
		argument_symbol_table.update({name: type})
	else:  # kind == 'VAR'
		var_symbol_table.update({name: type})
	return  # void


def var_count(kind):
	# returns the number of variables of the given kind already defined in the current scope
	global static_symbol_table
	global field_symbol_table
	global argument_symbol_table
	global var_symbol_table

	if kind == 'STATIC':
		return len(static_symbol_table)
	elif kind == 'FIELD':
		return len(field_symbol_table)
	elif kind == 'ARG':
		return len(argument_symbol_table)
	else:  # kind == 'VAR'
		return len(var_symbol_table)


def kind_of(name):
	# returns the kind of the named identifier in the current scope.
	# if the identifier is unknown in the current scope, return NONE.
	global static_symbol_table
	global field_symbol_table
	global argument_symbol_table
	global var_symbol_table

	if name in static_symbol_table:
		return 'STATIC'
	if name in field_symbol_table:
		return 'FIELD'
	if name in argument_symbol_table:
		return 'ARG'
	if name in var_symbol_table:
		return 'VAR'
	else:
		return 'NONE'


def type_of(name):
	# returns the type of the named identifier in the current scope
	global static_symbol_table
	global field_symbol_table
	global argument_symbol_table
	global var_symbol_table

	if name in static_symbol_table:
		return static_symbol_table.get(name)
	elif name in field_symbol_table:
		return field_symbol_table.get(name)
	elif name in argument_symbol_table:
		return argument_symbol_table.get(name)
	else:  # name in var_symbol_table:
		return var_symbol_table.get(name)


def index_of(name):
	# returns the index assigned to the named identifier
	global static_symbol_table
	global field_symbol_table
	global argument_symbol_table
	global var_symbol_table

	if name in static_symbol_table:
		return static_symbol_table.indexOf(name)
	elif name in field_symbol_table:
		return field_symbol_table.indexOf(name)
	elif name in argument_symbol_table:
		return argument_symbol_table.indexOf(name)
	else:  # name in var_symbol_table:
		return var_symbol_table.indexOf(name)


# VM Writer #############################
# segment => (CONST, ARG, LOCAL, STATIC, THIS, THAT, POINTER, TEMP)
# command => (String)


def write_push(segment, index):
	# writes a VM push command

	return 'push {!s} {!s}'.format(segment, index)


def write_pop(segment, index):
	# writes a VM pop command

	return 'pop {!s} {!s}'.format(segment, index)


def write_arithmetic(command):
	# writes a VM arithmetic command

	return command.lower()


def write_label(label):
	# writes a VM label command

	return 'label {!s}'.format(label)


def write_goto(label):
	# writes a VM goto command

	return 'goto {!s}'.format(label)


def write_if(label):
	# writes a VM if-goto command

	return 'if-goto {!s}'.format(label)


def write_call(name, nArgs):
	# writes a VM call command

	return 'call {!s} {!s}'.format(name, nArgs)


def write_function(name, nLocals):
	# writes a VM function command

	return 'function {!s} {!s}'.format(name, nLocals)


def write_return():
	# writes a VM function command

	return 'return'


#########################################
# Testing/Running Area ##################
#########################################


def main():
	global vm_output

	# Tokenize the Input File
	for file_path_counter in range(0, len(input_file_path_list)):
		tokenized_input_string = get_tokenized_input_as_string(get_file_lines_as_string(input_file_path_list[file_path_counter]))

		t_output_file = open(output_t_file_path_list[file_path_counter], 'w')
		t_output_file.write(tokenized_input_string)
		t_output_file.close()

	# Syntax Analysis of the Tokenized Input
	# Also contains to the process for the ch 11 .jack to .vm compiler
	for file_path_counter in range(0, len(output_t_file_path_list)):
		tokenized_input_string = get_file_lines_as_list(output_t_file_path_list[file_path_counter])
		syntax_analyzer_output = compile_class(get_token_value_pair_list(tokenized_input_string))

		syntax_analyzer_output_file = open(output_file_path_list[file_path_counter], 'w')
		syntax_analyzer_output_file.write(syntax_analyzer_output)
		syntax_analyzer_output_file.close()

		vm_output_file = open(output_vm_file_path_list[file_path_counter], 'w')
		vm_output_file.write(vm_output)
		vm_output_file.close()


main()

# TODO: What needs to get done:
# TODO: The compiler put together in chapter 10 needs to have sections added to it that call chapter 11 methods
# TODO: in order to add to the "vm_output" global string.
# TODO: For example, when compile_subroutine_dec is called, the symbol table should be wiped.
# TODO: Likewise, when compile_var_dex is called, the symbol table should be updated.
