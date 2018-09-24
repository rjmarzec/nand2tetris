#########################################
# Global Variables ######################
#########################################


# Th names of the files need to be manually changed here for different test to be run
input_file_name = "simpleAdd.vm"
output_file_name = "simpleAdd.asm"


#########################################
# Main Running Area #####################
#########################################


def vm_to_asm():
	input_file = open("test.vm", "r")
	raw_file_line_list = get_file_lines_as_list(input_file)
	cleaned_vm_line_list = clean_line_list(raw_file_line_list)
	hack_line_list = convert_vm_to_hack(cleaned_vm_line_list)
	write_hack_to_file(hack_line_list)


#########################################
# Function Area #########################
#########################################


def get_file_lines_as_list(input_file):
	return input_file.readlines()


def clean_line_list(input_line_list):
	result_line_list = []
	for line in input_line_list:
		# removes any spaces and instances of spaces, \n, \r, and \t
		temp_line = line
		temp_line = temp_line.replace("\n", "")
		temp_line = temp_line.replace("\r", "")
		temp_line = temp_line.replace("\t", "")

		# removes any comments from a line if they exist
		if "//" in temp_line:
			temp_line = temp_line[:temp_line.index("//")]

		# clears any starting and ending spaces
		temp_line.strip()

		# turns any spaces longer than 1 space into 1 space
		while "  " in temp_line:
			temp_line.replace("  ", " ")

		# ignores the line if there is no actual code on it
		if temp_line != "":
			result_line_list.append(temp_line)
	return result_line_list


def convert_vm_to_hack(input_line_list):
	result_line_list = []

	for line in input_line_list:
		line_command_type = get_command_type(line)
		result_line = convert_line_to_hack(line, line_command_type)
		result_line_list.append(result_line)

	return result_line_list


def get_command_type(input_line):
	if "add" or "sub":
		# add more artimethic commands to the if statement
		return "C_ARITHMETIC"
	elif "push" in input_line:
		return "C_POP"
	elif "pop" in input_line:
		return "C_PUSH"
	elif "label" in input_line:
		return "C_GOTO"
	elif "if" in input_line:
		return "C_IF"
	elif "function" in input_line:
		return "C_FUNCTION"
	elif "return" in input_line:
		return "C_RETURN"
	else:
		# elif "call" in line:
		return "C_CALL"


def convert_line_to_hack(input_line, command_type):
	if command_type == "C_ARITHMETIC":
		return write_arithmetic(input_line)
	elif command_type == "C_PUSH" or command_type == "C_POP":
		return write_push_pop(input_line, command_type)
	elif command_type == "C_LABEL":
		return
	elif command_type == "C_GOTO":
		return
	elif command_type == "C_IF":
		return
	elif command_type == "C_FUNCTION":
		return
	elif command_type == "C_RETURN":
		return
	elif command_type == "C_CALL":
		return
	else:
		return "ERROR: Command not specified"


# TODO: finish up adding and subtracting here after getting push/pop to work
def write_arithmetic(input_line):
	result_string = ""
	if "add" in input_line:
		result_string += \
			"@SP" \
			"D=M" \
			""
	elif "sub" in input_line:
		result_string += "tempSubText"
	return result_string


def write_push_pop(input_line, command_type):
	result_string = ""
	edited_string = ""
	if command_type == "C_PUSH":
		# editedString =
		# resultString
		return
	elif command_type == "C_POP":
		return
	return result_string


#########################################
# Testing Area ##########################
#########################################


def write_hack_to_file(input_line_list):
	output_file = open("test.asm", "w")
	writeString = ""
	for line in input_line_list:
		writeString += line + "\n"
	# writeString += str(line)
	file.write(writeString)
	file.close()


vm_to_asm()
