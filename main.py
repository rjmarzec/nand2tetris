#########################################
# Global Variables ######################
#########################################

# Th names of the files need to be manually changed here for different tests to be run
input_file_name = "testFiles/simpleAdd/simpleAdd.vm"
output_file_name = "testFiles/simpleAdd/simpleAdd.asm"


#########################################
# Main Running Area #####################
#########################################


def vm_to_asm():
	global input_file_name
	input_file = open(input_file_name, "r")
	raw_file_line_list = get_file_lines_as_list(input_file)
	cleaned_vm_line_list = clean_line_list(raw_file_line_list)
	hack_line_list = convert_vm_to_hack(cleaned_vm_line_list)
	write_hack_to_file(hack_line_list)


#########################################
# Cleanup and Convert Functions #########
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
	if "add" in input_line or "sub" in input_line:
		# add more arithmetic commands to the if statement
		return "C_ARITHMETIC"
	elif "push" in input_line:
		return "C_PUSH"
	elif "pop" in input_line:
		return "C_POP"
	elif "label" in input_line:
		return "C_GOTO"
	elif "if" in input_line:
		return "C_IF"
	elif "function" in input_line:
		return "C_FUNCTION"
	elif "return" in input_line:
		return "C_RETURN"
	elif "call" in input_line:
		return "C_CALL"
	else:
		print("ERROR: Command type not specified")
		return "C_ERROR"


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
		return "ERROR: Command not specified?"


# Arithmetic Code #######################


def write_arithmetic(input_line):
	result_string = ""
	if "add" in input_line:
		# Get the location the stack pointer is pointing, store it, and bump it down by 1
		result_string += "@SP" + "\n"
		result_string += "D=M" + "\n"
		result_string += "M=M-1" + "\n"

		# Move to the stack pointer

	elif "sub" in input_line:
		result_string += "tempSubText"
	return result_string


# Push/Pop Code #########################


def write_push_pop(input_line, command_type):
	segment_pointer_type = get_segment_pointer_type(input_line)
	push_pop_value = remove_segment_pointer_and_earlier(input_line, segment_pointer_type).strip()
	result_string = ""

	if command_type == "C_PUSH":
		# Access the value we want to push, and store that value for later
		result_string += "@" + push_pop_value + "\n"
		result_string += "D=A" + "\n"

		# Access the the pointer location and bump up for the next time the stack is called
		result_string += "@" + segment_pointer_type + "\n"
		result_string += "M=M+1" + "\n"

		# Move to the location that the stack pointer referred to before getting bumped up
		result_string += "A=M-1" + "\n"

		# Store the push value at the top of the stack
		result_string += "M=D" + "\t\t//" + input_line

		return result_string
	elif command_type == "C_POP":
		input_minus_pop = input_line[input_line.find("pop"):]
		result_string = "temp pop result code"
		return result_string
	return "ERROR: failure when writing push/pop"


# Segment Pointer Code


def get_segment_pointer_type(input_line):
	if "constant" in input_line:
		return "SP"
	elif "local" in input_line:
		return "LCL"
	elif "argument" in input_line:
		return "ARG"
	elif "this" in input_line:
		return "THIS"
	elif "that" in input_line:
		return "THAT"
	return "ERROR: failure when finding pointer segment type"


def remove_segment_pointer_and_earlier(input_line, segment_pointer_type):
	if segment_pointer_type == "SP":
		return input_line[input_line.find("constant") + len("constant"):]
	elif segment_pointer_type == "LCL":
		return input_line[input_line.find("local"):]
	elif segment_pointer_type == "ARG":
		return input_line[input_line.find("argument"):]
	elif segment_pointer_type == "THIS":
		return input_line[input_line.find("this"):]
	elif segment_pointer_type == "THAT":
		return input_line[input_line.find("that"):]
	return "ERROR: Did not find pointer type"


#########################################
# Testing Area ##########################
#########################################


def write_hack_to_file(input_line_list):
	global output_file_name
	output_file = open(output_file_name, "w")
	write_string = ""
	for line in input_line_list:
		write_string += line + "\n"
	# writeString += str(line)
	output_file.write(write_string)
	output_file.close()


vm_to_asm()
