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

def get_file_lines_as_list(file_path):
	input_file = open(file_path, "r")
	result_list = input_file.readlines()
	input_file.close()

	return result_list


def other_function(variable_input):
	print('temp"')
	return


#########################################
# Testing Area ##########################
#########################################

print(file_name_constants.ARRAY_TEST_IN[0])
