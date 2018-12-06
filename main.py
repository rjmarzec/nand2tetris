import file_name_constants

#########################################
# Global Variables ######################
#########################################

# TODO: http://nand2tetris-questions-and-answers-forum.32033.n3.nabble.com/Global-Stack-Clarification-td4026677.html
# TODO: ^^^ look into this because it might help to figure out the problem
# These variables need to be changed to run different test. Refer to the constants file for the names
input_file_name = file_name_constants.SIMPLE_FUNCTION_IN
output_file_name = file_name_constants.SIMPLE_FUNCTION_OUT

# Used later for writing jumps in our asm code so that they don't repeat
asm_jump_counter = 0

# Used later in our return addresses so they don't repeat
return_address_counter = 0

# A list of all the arithmetic functions to make them easy to reference
arithmetic_function_list = ["add", "sub", "neg", "eq", "lt", "gt", "and", "or", "not"]


#########################################
# Cleanup and Start Functions ###########
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
		temp_line = temp_line.strip()

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
	if input_line in arithmetic_function_list:
		return "C_ARITHMETIC"
	elif "push" in input_line:
		return "C_PUSH"
	elif "pop" in input_line:
		return "C_POP"
	elif "label" in input_line:
		return "C_LABEL"
	elif "if-goto" in input_line:
		return "C_IF"
	elif "goto" in input_line:
		return "C_GOTO"
	elif "function" in input_line:
		return "C_FUNCTION"
	elif "return" in input_line:
		return "C_RETURN"
	elif "call" in input_line:
		return "C_CALL"
	elif "label" in input_line:
		return "C_LABEL"
	else:
		print("ERROR: Command type not specified")
		return "C_ERROR"


def convert_line_to_hack(input_line, command_type):
	if command_type == "C_ARITHMETIC":
		return write_arithmetic(input_line)
	elif command_type == "C_PUSH" or command_type == "C_POP":
		return write_push_pop(input_line, command_type)
	elif command_type == "C_LABEL":
		return write_label(input_line)
	elif command_type == "C_IF":
		return write_if_goto(input_line)
	elif command_type == "C_GOTO":
		return write_goto(input_line)
	elif command_type == "C_FUNCTION":
		return write_function(input_line)
	elif command_type == "C_RETURN":
		return write_return(input_line)
	elif command_type == "C_CALL":
		return write_call(input_line)
	else:
		return "ERROR: Command not specified?"


#########################################
# Code Conversion Functions #############
#########################################


def write_arithmetic(input_line):
	result_string = ""
	# The first line of each if statement describes what the result of the operation should look like
	# y = M(@SP) - 1, and x = M(@SP) - 2
	if "add" in input_line:
		# x + y

		# Get the location the stack pointer is pointing
		result_string += "@" + pointer_type_to_ram_address("SP") + "\n"

		# Change the value of the stack pointer down one to where it should be after the computation
		result_string += "M=M-1" + "\n"

		# Move to where the stack pointer points to and store the value of the register at that point
		result_string += "A=M" + "\n"
		result_string += "D=M" + "\n"

		# Move to the point before the previous value, add the two together, and store the result there
		result_string += "A=A-1" + "\n"
		result_string += "M=D+M" + "\t//" + input_line
	elif "sub" in input_line:
		# x - y

		# Get the location the stack pointer is pointing
		result_string += "@" + pointer_type_to_ram_address("SP") + "\n"

		# Change the value of the stack pointer down one to where it should be after the computation
		result_string += "M=M-1" + "\n"

		# Move to the value before where the stack pointer points to and store the value of the register at that point
		result_string += "A=M-1" + "\n"
		result_string += "D=M" + "\n"

		# Move back up to the value we want to be subtracting, subtract the two in D and M, and store it to D
		result_string += "A=A+1" + "\n"
		result_string += "D=D-M" + "\n"

		# Store the value of the subtraction from D to where it should be in the stack
		result_string += "A=A-1" + "\n"
		result_string += "M=D" + "\t\t//" + input_line
	elif "neg" in input_line:
		# - y

		# Get the location in the stack where y is stored
		result_string += "@" + pointer_type_to_ram_address("SP") + "\n"
		result_string += "A=M-1" + "\n"

		# Negate y and save it to where it should be
		result_string += "M=-M" + "\t\t//" + input_line
	elif "eq" in input_line or "gt" in input_line or "lt" in input_line:
		global asm_jump_counter
		# this first section gives us x - y, which is useful later

		# Access the stack pointer and bump it to where it should be after the operation
		result_string += "@" + pointer_type_to_ram_address("SP") + "\n"
		result_string += "M=M-1" + "\n"
		result_string += "A=M-1" + "\n"

		# Store x, move to y, and store (x - y) to D
		result_string += "D=M" + "\n"
		result_string += "A=A+a1" + "\n"
		result_string += "D=D-M" + "\n"

		# Continue with whatever function we want to do:
		if "eq" in input_line:
			# true (-1) if x = y, false (0) otherwise

			# Subtract the two values and check if the result is equal to 0
			result_string += "@EQJUMP" + str(asm_jump_counter) + "\n"

			# Jump ahead if the values are not equal
			result_string += "D;JNE" + "\n"

			# This only runs if the values are equal
			result_string += "@" + pointer_type_to_ram_address("SP") + "\n"
			result_string += "A=M-1" + "\n"
			result_string += "M=-1" + "\n"

			# After this section executes, jump passed the code below
			result_string += "@EQFINISH" + str(asm_jump_counter) + "\n"
			result_string += "0;JMP" + "\n"

			# Jump to this line if the the values are not equal
			result_string += "(EQJUMP" + str(asm_jump_counter) + ")" + "\n"

			# This only runs if the values are not equal
			result_string += "@" + pointer_type_to_ram_address("SP") + "\n"
			result_string += "A=M-1" + "\n"
			result_string += "M=0" + "\n"

			# Jump to this line when we are done with the comparison
			result_string += "(EQFINISH" + str(asm_jump_counter) + ")" + "\t//eq"
		elif "gt" in input_line:
			# true (-1) if x > y, false (0) otherwise
			# true (-1) if (x - y) > 0, false (0) otherwise

			# Check if the result is greater than 0
			result_string += "@GTJUMP" + str(asm_jump_counter) + "\n"

			# Jump ahead if the result is NOT greater than 0
			result_string += "D;JLE" + "\n"

			# This only runs the result is greater than 0
			result_string += "@" + pointer_type_to_ram_address("SP") + "\n"
			result_string += "A=M-1" + "\n"
			result_string += "M=-1" + "\n"

			# After this section executes, jump passed the code below
			result_string += "@GTFINISH" + str(asm_jump_counter) + "\n"
			result_string += "0;JMP" + "\n"

			# Jump to this line if the the resulting value is not greater than 0
			result_string += "(GTJUMP" + str(asm_jump_counter) + ")" + "\n"

			# This only runs if the result is not greater than 0
			result_string += "@" + pointer_type_to_ram_address("SP") + "\n"
			result_string += "A=M-1" + "\n"
			result_string += "M=0" + "\n"

			# Jump to this line when we are done with the comparison
			result_string += "(GTFINISH" + str(asm_jump_counter) + ")" + "\t//gt"
		elif "lt" in input_line:
			# true (-1) if x < y, false (0) otherwise
			# true (-1) if (x - y) < 0, false (0) otherwise

			# Check if the result is less than 0
			result_string += "@LTJUMP" + str(asm_jump_counter) + "\n"

			# Jump ahead if the result is NOT less than 0
			result_string += "D;JGE" + "\n"

			# This only runs if the result is less than 0
			result_string += "@" + pointer_type_to_ram_address("SP") + "\n"
			result_string += "A=M-1" + "\n"
			result_string += "M=-1" + "\n"

			# After this section executes, jump passed the code below
			result_string += "@LTFINISH" + str(asm_jump_counter) + "\n"
			result_string += "0;JMP" + "\n"

			# Jump to this line if the the result is not less than 0
			result_string += "(LTJUMP" + str(asm_jump_counter) + ")" + "\n"

			# This only runs if the result is not less than 0
			result_string += "@" + pointer_type_to_ram_address("SP") + "\n"
			result_string += "A=M-1" + "\n"
			result_string += "M=0" + "\n"

			# Jump to this line when we are done with the comparison
			result_string += "(LTFINISH" + str(asm_jump_counter) + ")" + "\t//lt"
		# Bump up the counter so that are jumps are not repeated
		asm_jump_counter += 1
	elif "and" in input_line:
		# x And y (bit-wise)

		# Access the stack pointer and bump it to where it should be after the operation
		result_string += "@" + pointer_type_to_ram_address("SP") + "\n"
		result_string += "M=M-1" + "\n"
		result_string += "A=M" + "\n"

		# Store y and move to x
		result_string += "D=M" + "\n"
		result_string += "A=A-1" + "\n"

		# And the two together and store it to x
		result_string += "M=D&M" + "\t//and"
	elif "or" in input_line:
		# x Or y (bit-wise)

		# Access the stack pointer and bump it to where it should be after the operation
		result_string += "@" + pointer_type_to_ram_address("SP") + "\n"
		result_string += "M=M-1" + "\n"
		result_string += "A=M" + "\n"

		# Store y and move to x
		result_string += "D=M" + "\n"
		result_string += "A=A-1" + "\n"

		# Or the two together and store it to x
		result_string += "M=D|M" + "\t//or"
	elif "not" in input_line:
		# Not y (bit-wise)

		# Access the stack pointer and go to the point before it
		result_string += "@" + pointer_type_to_ram_address("SP") + "\n"
		result_string += "A=M-1" + "\n"

		# Not the value at that point and store it back to where we got it
		result_string += "D=M" + "\n"
		result_string += "M=!D" + "\t//not"
	else:
		result_string += "ERROR: tried to write arithmetic but command was not found"
		result_string += "" # This line is here so that I can close this else statement in the IDE
	return result_string


def write_push_pop(input_line, command_type):
	segment_pointer_type = get_segment_pointer_type(input_line)
	push_pop_value = remove_segment_pointer_and_earlier(input_line, segment_pointer_type).strip()
	result_string = ""

	if command_type == "C_PUSH":
		# the static keyword is a bit funky, so we have to handle thing differently if it comes up
		if segment_pointer_type == "STATIC":
			# For the statement "push static z",
			# access static(z) and put that value to the top of the SP stack

			# Access the value we want to push, and store that value for later
			result_string += "@" + str(int(push_pop_value) + 16) + "\n"
			result_string += "D=M" + "\n"

			# Access the the pointer location and bump up for the next time the stack is called
			result_string += "@" + pointer_type_to_ram_address("SP") + "\n"
			result_string += "M=M+1" + "\n"

			# Move to the location that the stack pointer referred to before getting bumped up
			result_string += "A=M-1" + "\n"

			# Store the push value at the top of the stack
			result_string += "M=D"
		# Pointer refers to 2 register, so we handle it differently. same idea for "Temp"
		elif segment_pointer_type == "POINTER" or segment_pointer_type == "TEMP":
			# For the statement "push pointer z" (where z is 1 or 2),
			# access static(z) and put that value to the top of the SP stack

			# Access the value we want to push, and store that value for later
			if segment_pointer_type == "POINTER":
				result_string += "@" + str(int(push_pop_value) + 3) + "\n"
			else:
				result_string += "@" + str(int(push_pop_value) + 5) + "\n"
			result_string += "D=M" + "\n"

			# Access the the pointer location and bump it up for the next time the stack is called
			result_string += "@" + pointer_type_to_ram_address("SP") + "\n"
			result_string += "M=M+1" + "\n"

			# Move to the location that the stack pointer referred to before getting bumped up
			result_string += "A=M-1" + "\n"

			# Store the push value at the top of the stack
			result_string += "M=D"
		elif segment_pointer_type == "SP":
			# Access the value we want to push, and store that value for later
			result_string += "@" + push_pop_value + "\n"
			result_string += "D=A" + "\n"

			# Access the the pointer location and bump up for the next time the stack is called
			result_string += "@" + pointer_type_to_ram_address(segment_pointer_type) + "\n"
			result_string += "M=M+1" + "\n"

			# Move to the location that the stack pointer referred to before getting bumped up
			result_string += "A=M-1" + "\n"

			# Store the push value at the top of the stack
			result_string += "M=D"
		elif segment_pointer_type == "ARG":
			# Take the value from M(A(ARG) + push_pop_value) and store it to the stop of the stack
			result_string += "@" + push_pop_value + "\n"
			result_string += "D=A" + "\n"

			result_string += "@" + pointer_type_to_ram_address(segment_pointer_type) + "\n"
			result_string += "A=D+M" + "\n"
			result_string += "D=M" + "\n"

			result_string += "@" + pointer_type_to_ram_address("SP") + "\n"
			result_string += "M=M+1" + "\n"
			result_string += "A=M-1" + "\n"
			result_string += "M=D"
		else:
			# For push this/that x:
			# Take the value from M(3/4 + x) and put it at the top of the SP stack

			# Add the push pop value to the stack register so we can access the location without big shenanigans
			result_string += "@" + push_pop_value + "\n"
			result_string += "D=A" + "\n"
			result_string += "@" + pointer_type_to_ram_address(segment_pointer_type) + "\n"
			result_string += "M=D+M" + "\n"

			# Get the address from that location and store it to be placed at the top of the stack
			result_string += "A=M" + "\n"
			result_string += "D=M" + "\n"

			# Go to the top of the SP stack and bump it up for the next usage of it
			result_string += "@" + pointer_type_to_ram_address("SP") + "\n"
			result_string += "M=M+1" + "\n"

			# Put the value stored in D stored at the current top of the stack
			result_string += "A=M-1" + "\n"
			result_string += "M=D" + "\n"

			# Subtract the push pop value from the stack register to undo what we did at the start
			result_string += "@" + push_pop_value + "\n"
			result_string += "D=-A" + "\n"
			result_string += "@" + pointer_type_to_ram_address(segment_pointer_type) + "\n"
			result_string += "M=D+M"
		return result_string + "\t\t//" + input_line
	elif command_type == "C_POP":
		# the static pointer is a bit funky so we have to make this section different for it
		if segment_pointer_type == "STATIC":
			# For the statement "pop static z",
			# take the value at the stop of the SP stack and store it to static(z)

			# Access the pointer location and bump down for the next time the stack is called
			result_string += "@" + pointer_type_to_ram_address("SP") + "\n"
			result_string += "M=M-1" + "\n"

			# Store the value that was at the top of the stack
			result_string += "A=M" + "\n"
			result_string += "D=M" + "\n"

			# Access the register where we want to store the value and store it there
			result_string += "@" + str(int(push_pop_value) + 16) + "\n"
			result_string += "M=D"
		elif segment_pointer_type == "POINTER" or segment_pointer_type == "TEMP":
			# For the statement "pop pointer z",
			# take the value at the stop of the SP stack and store it to pointer(z)

			# Access the SP pointer location and bump down for the next time the stack is called
			result_string += "@" + pointer_type_to_ram_address("SP") + "\n"
			result_string += "M=M-1" + "\n"

			# Store the value that was at the top of the stack
			result_string += "A=M" + "\n"
			result_string += "D=M" + "\n"

			# Access the register where we want to store the value and store it there
			if segment_pointer_type == "POINTER":
				result_string += "@" + str(int(push_pop_value) + 3) + "\n"
			else:
				result_string += "@" + str(int(push_pop_value) + 5) + "\n"
			result_string += "M=D"
		elif segment_pointer_type == "SP":
			# Access the pointer location and bump down for the next time the stack is called
			result_string += "@" + pointer_type_to_ram_address(
				segment_pointer_type) + "\n"
			result_string += "M=M-1" + "\n"

			# Store the value that was at the top of the stack before we moved the pointer
			result_string += "A=A+1" + "\n"
			result_string += "D=M" + "\n"

			# Access the register where we want to store the value and store it there
			result_string += "@R" + push_pop_value + "\n"
			result_string += "M=D"
		else:
			# For pop this/that x:
			# Take the value at the top of the stack and store it to M(3/4 + x)

			# Add the push pop value to the stack register so we can access the location without big shenanigans
			result_string += "@" + push_pop_value + "\n"
			result_string += "D=A" + "\n"
			result_string += "@" + pointer_type_to_ram_address(segment_pointer_type) + "\n"
			result_string += "M=D+M" + "\n"

			# Access the SP pointer location and bump down for the next time the stack is called
			result_string += "@" + pointer_type_to_ram_address("SP") + "\n"
			result_string += "M=M-1" + "\n"

			# Store the value that was at the top of the stack before we moved the pointer
			result_string += "A=M" + "\n"
			result_string += "D=M" + "\n"

			# Get the address we are storing the value to and store it there
			result_string += "@" + pointer_type_to_ram_address(segment_pointer_type) + "\n"
			result_string += "A=M" + "\n"
			result_string += "M=D" + "\n"

			# Subtract the push pop value from the stack register to undo what we did at the start
			result_string += "@" + push_pop_value + "\n"
			result_string += "D=-A" + "\n"
			result_string += "@" + pointer_type_to_ram_address(segment_pointer_type) + "\n"
			result_string += "M=D+M"
		return result_string + "\t\t//" + input_line
	return "ERROR: failure when writing push/pop"


def write_label(input_line):
	return "(" + input_line[len("label "):] + ")" + "\t//" + input_line


def write_if_goto(input_line):
	# Pop the value from the top of the stack, and jump back to the label if the value is NOT 0
	label_name = input_line[input_line.find("goto") + len("goto"):].strip()

	# Get the location the stack pointer is pointing
	result_string = "@" + pointer_type_to_ram_address("SP") + "\n"

	# Change the value of the stack pointer down one to where it should be after the computation
	result_string += "M=M-1" + "\n"

	# Move to where the stack pointer points to and store the value of the register at that point
	result_string += "A=M" + "\n"
	result_string += "D=M" + "\n"

	# Jump to the label if the value stored in D is not 0
	result_string += "@" + label_name + "\n"
	result_string += "D;JNE"

	return result_string + "\t//" + input_line


def write_goto(input_line):
	# Jump to the label provided always
	label_name = input_line[input_line.find("goto") + len("goto"):].strip()

	result_string = "@" + label_name + "\n"
	result_string += "D;JMP"

	return result_string + "\t//" + input_line


def write_call(input_line):
	# This function should generate the following .asm code:
	"""
	push return-address
	push LCL
	push ARG
	push THIS
	push THAT
	ARG = SP-n-5
	LCL = SP
	goto f
	(return-address) [as a label]
	"""

	global return_address_counter

	# This gives us "[call][f][n]" from the input line formatted as "call f n"
	call_line_as_list = input_line.split(" ")

	return_address_label_name = "RETURNADDRESS" + str(return_address_counter)

	result_string = write_push_return_address(return_address_label_name)
	result_string += write_register_push("LCL")
	result_string += write_register_push("ARG")
	result_string += write_register_push("THIS")
	result_string += write_register_push("THAT")
	result_string += write_sp_n_5_to_arg(call_line_as_list[2])
	result_string += write_sp_to_lcl()
	result_string += write_goto(call_line_as_list[1]) + "\n"
	result_string += "(" + return_address_label_name + ")"
	return_address_counter += 1

	# return result_string + "\t//" + input_line
	return result_string + "\t//" + input_line


def write_function(input_line):
	# This function should generate the following .asm code:
	"""
	(f)	[as a label for function entry]
	repeat k times:
	push 0
	"""

	# This gives us "[function][f][k]" from the input line formatted as "function f k"
	function_line_as_list = input_line.split(" ")

	result_string = "(" + function_line_as_list[1] + ")"
	for i in range(int(function_line_as_list[2])):
		# Pushing 0 to the top of the stack here
		result_string += "\n@" + pointer_type_to_ram_address("SP") + "\n"
		result_string += "M=M+1" + "\n"
		result_string += "A=M-1" + "\n"
		result_string += "M=0"

	return result_string + "\t\t//" + input_line


def write_return(input_line):
	# This function should generate the following .asm code:
	"""
	FRAME = LCL			{FRAME is a temp variable, will be @R13 for this}
	RET = *(FRAME-5) 	{RET = return address, will be @R14 for this}
	*ARG = pop()
	SP = ARG+1
	THAT = *(FRAME-1)	{*(...) means the pointer to that value}
	THIS = *(FRAME-2)
	ARG = *(FRAME-3)
	LCL = *(FRAME-4)
	goto RET
	"""

	# FRAME = LCL
	result_string = "@" + pointer_type_to_ram_address("LCL") + "\n"
	result_string += "D=M" + "\n"

	result_string += "@13" + "\n"
	result_string += "M=D" + "\n"

	# RET = *(FRAME-5)
	result_string += "@13" + "\n"
	result_string += "D=M" + "\n"

	result_string += "@5" + "\n"
	result_string += "D=D-A" + "\n"

	result_string += "A=D" + "\n"
	result_string += "D=M" + "\n"

	result_string += "@14" + "\n"
	result_string += "M=D" + "\n"

	# *ARG = pop()
	# Is effectively "pop argument 0"
	result_string += "@" + pointer_type_to_ram_address("ARG") + "\n"
	result_string += "A=M" + "\n"
	result_string += "D=M" + "\n"

	result_string += "@" + pointer_type_to_ram_address("SP") + "\n"
	result_string += "M=M+1" + "\n"
	result_string += "A=M-1" + "\n"
	result_string += "M=D" + "\n"

	# SP = ARG + 1
	# Is really ARG = M(SP) - 1?
	# TODO: This might be the problem? I honestly don't know what it needs to be.
	# TODO: Note: the problem is still R(310) not changing.
	"""
	result_string += "@" + pointer_type_to_ram_address("SP") + "\n"
	result_string += "A=M" + "\n"
	result_string += "A=A-1" + "\n"
	result_string += "D=M" + "\n"

	result_string += "@" + pointer_type_to_ram_address("ARG") + "\n"
	result_string += "M=D" + "\n"
	"""

	result_string += "@" + pointer_type_to_ram_address("ARG") + "\n"
	result_string += "D=M+1" + "\n"

	result_string += "@" + pointer_type_to_ram_address("SP") + "\n"
	result_string += "M=D" + "\n"

	# THAT = *(FRAME - 1)
	result_string += "@13" + "\n"
	result_string += "D=M" + "\n"

	result_string += "@1" + "\n"
	result_string += "D=D-A" + "\n"

	result_string += "A=D" + "\n"
	result_string += "D=M" + "\n"

	result_string += "@14" + "\n"
	result_string += "M=D" + "\n"

	result_string += "@" + pointer_type_to_ram_address("THAT") + "\n"
	result_string += "M=D" + "\n"

	# THIS = *(FRAME - 2)
	result_string += "@13" + "\n"
	result_string += "D=M" + "\n"

	result_string += "@2" + "\n"
	result_string += "D=D-A" + "\n"

	result_string += "A=D" + "\n"
	result_string += "D=M" + "\n"

	result_string += "@14" + "\n"
	result_string += "M=D" + "\n"

	result_string += "@" + pointer_type_to_ram_address("THIS") + "\n"
	result_string += "M=D" + "\n"

	# ARG = *(FRAME - 3)
	result_string += "@13" + "\n"
	result_string += "D=M" + "\n"

	result_string += "@3" + "\n"
	result_string += "D=D-A" + "\n"

	result_string += "A=D" + "\n"
	result_string += "D=M" + "\n"

	result_string += "@14" + "\n"
	result_string += "M=D" + "\n"

	result_string += "@" + pointer_type_to_ram_address("ARG") + "\n"
	result_string += "M=D" + "\n"

	# LCL = *(FRAME - 4)
	result_string += "@13" + "\n"
	result_string += "D=M" + "\n"

	result_string += "@4" + "\n"
	result_string += "D=D-A" + "\n"

	result_string += "A=D" + "\n"
	result_string += "D=M" + "\n"

	result_string += "@14" + "\n"
	result_string += "M=D" + "\n"

	result_string += "@" + pointer_type_to_ram_address("LCL") + "\n"
	result_string += "M=D" + "\n"

	# goto RET
	result_string += "@14" + "\n"
	result_string += "A=M" + "\n"
	result_string += "0;JMP"

	return result_string + "\t\t//" + input_line


def write_register_pop(register_address):
	# Go to the provided register, take it's value, and plop it at the top of the stack
	result_string = "@" + str(register_address) + "\n"

	result_string += "D=M" + "\n"

	result_string += "@" + pointer_type_to_ram_address("SP") + "\n"
	result_string += "M=M+1" + "\n"
	result_string += "A=M-1" + "\n"
	result_string += "M=D" + "\n"

	return result_string


def write_register_push(register_address):
	# Go to the top of the stack, bump the pointer down, store the value there, and store it to the passed in register
	result_string = "@" + pointer_type_to_ram_address("SP") + "\n"

	result_string += "M=M-1" + "\n"

	result_string += "A=M" + "\n"
	result_string += "D=M" + "\n"

	# Take the stored value and store it to the passed in address
	result_string += "@" + str(register_address) + "\n"
	result_string += "M=D"

	return result_string + "\n"


def write_sp_n_5_to_arg(n_value):
	# This does ARG = SP-n-5

	result_string = "@" + pointer_type_to_ram_address("SP") + "\n"
	result_string += "D=A" + "\n"
	result_string += "@" + str(n_value) + "\n"
	result_string += "D=D-A" + "\n"
	result_string += "@5" + "\n"
	result_string += "D=D-A" + "\n"

	result_string += "@" + pointer_type_to_ram_address("ARG") + "\n"
	result_string += "M=D"
	return result_string + "\n"


def write_sp_to_lcl():
	result_string = "@" + pointer_type_to_ram_address("SP") + "\n"
	result_string += "D=A" + "\n"
	result_string += "@" + pointer_type_to_ram_address("ARG") + "\n"
	result_string += "M=D" + "\n"
	return result_string + "\n"


def write_push_return_address(return_address_label_name):
	result_string = "@" + return_address_label_name + "\n"
	result_string += "D=A" + "\n"
	result_string += "@" + pointer_type_to_ram_address("SP") + "\n"
	result_string += "M=M+1" + "\n"
	result_string += "A=M-1" + "\n"
	result_string += "M=D"
	return result_string + "\n"


#########################################
# Segment Pointer Function ##############
#########################################


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
	elif "pointer" in input_line:
		return "POINTER"
	elif "static" in input_line:
		return "STATIC"
	elif "temp" in input_line:
		return "TEMP"
	return "ERROR: could not find pointer type"


def remove_segment_pointer_and_earlier(input_line, segment_pointer_type):
	if segment_pointer_type == "SP":
		return input_line[input_line.find("constant") + len("constant"):]
	elif segment_pointer_type == "LCL":
		return input_line[input_line.find("local") + len("local"):]
	elif segment_pointer_type == "ARG":
		return input_line[input_line.find("argument") + len("argument"):]
	elif segment_pointer_type == "THIS":
		return input_line[input_line.find("this") + len("this"):]
	elif segment_pointer_type == "THAT":
		return input_line[input_line.find("that") + len("that"):]
	elif segment_pointer_type == "STATIC":
		return input_line[input_line.find("static") + len("static"):]
	elif segment_pointer_type == "POINTER":
		return input_line[input_line.find("pointer") + len("pointer"):]
	elif segment_pointer_type == "POINTER":
		return input_line[input_line.find("pointer") + len("pointer"):]
	elif segment_pointer_type == "TEMP":
		return input_line[input_line.find("temp") + len("temp"):]
	return "ERROR: could not find pointer type"


def pointer_type_to_ram_address(segment_pointer_type):
	if segment_pointer_type == "SP":
		return "R0"
	elif segment_pointer_type == "LCL":
		return "R1"
	elif segment_pointer_type == "ARG":
		return "R2"
	elif segment_pointer_type == "THIS":
		return "R3"
	elif segment_pointer_type == "THAT":
		return "R4"
	elif segment_pointer_type == "POINTER":
		return "R3"
	elif segment_pointer_type == "TEMP":
		return "R5"
	# temp takes registers 5 to 12
	# 13 to 15 are used for general purpose functions by the VM implementation
	# static refers to the ram addresses starting at R16
	else:
		return "ERROR: register for pointer type not found"


def set_up_stack_pointer():
	# result_string = "@256" + "\n"
	result_string = "@16" + "\n"
	result_string += "D=A" + "\n"
	result_string += "@0" + "\n"
	result_string += "M=D" + "\n"
	return result_string


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


def write_hack_to_file(input_line_list):
	global output_file_name
	output_file = open(output_file_name, "w")
	# This line messes up some of the provided tests, so for now it's commented out
	# write_string = set_up_stack_pointer()
	write_string = ""
	for line in input_line_list:
		write_string += line + "\n"
	output_file.write(write_string)
	output_file.close()


#########################################
# Testing Area ##########################
#########################################


vm_to_asm()
