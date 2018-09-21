
#########################################
########## Main Running Area ############
#########################################

def vmToASM():
    file = open("test.vm", "r")
    rawFileLineList = getFileLinesAsList(file)
    cleanedVMLineList = cleanLineList(rawFileLineList)
    hackLineList = convertVMToHack(cleanedVMLineList)
    writeHackToFile(hackLineList)

#########################################
############ Function Area ##############
#########################################

def getFileLinesAsList(inputFile):
    return inputFile.readlines()


def cleanLineList(inputLineList):
    resultLineList = []
    for line in inputLineList:
        #removes any spaces and instances of spaces, \n, \r, and \t
        tempLine = line
        tempLine = tempLine.replace("\n", "")
        tempLine = tempLine.replace("\r", "")
        tempLine = tempLine.replace("\t", "")

        #removes any comments from a line if they exist
        if "//" in tempLine:
            tempLine = tempLine[:tempLine.index("//")]

        #clears any starting and ending spaces
        tempLine.strip()

        #turns any spaces longer than 1 space into 1 space
        while "  " in tempLine:
            tempLine.replace("  ", " ")

        #ignores the line if there is no actual code on it
        if tempLine != "":
            resultLineList.append(tempLine)
    return resultLineList


def convertVMToHack(inputLineList):
    resultLineList = []

    for line in inputLineList:
        resultLine = ""
        lineCommandType = getCommandType(line)
        resultLine = convertLineToHack(line, lineCommandType)
        resultLineList.append(resultLine)

    return resultLineList


def getCommandType(inputLine):
    if "add" or "sub":
        #add more artimethic commands to the if statement
        return "C_ARITHMETIC"
    elif "push" in inputLine:
        return "C_POP"
    elif "pop" in inputLine:
        return "C_PUSH"
    elif "label" in inputLine:
        return "C_GOTO"
    elif "if" in inputLine:
        return "C_IF"
    elif "function" in inputLine:
        return "C_FUNCTION"
    elif "return" in inputLine:
        return "C_RETURN"
    else:
        #elif "call" in line:
        return "C_CALL"


def convertLineToHack(inputLine, commandType):
    if commandType == "C_ARITHMETIC":
        return writeArithmetic(inputLine, commandType)
    elif commandType == "C_PUSH" or commandType == "C_POP":
        return writePushPop(inputLine, commandType)
    elif commandType == "C_LABEL":
        return
    elif commandType == "C_GOTO":
        return
    elif commandType == "C_IF":
        return
    elif commandType == "C_FUNCTION":
        return
    elif commandType == "C_RETURN":
        return
    elif commandType == "C_CALL":
        return
    else:
        return "ERROR: Command not specified"


def writeArithmetic(inputLine, commandType):
	resultString = ""
	if "add" in inputLine:
		resultString += "tempAddText"
	elif "sub" in inputLine:
		resultString += "tempSubText"
	return resultString


def writePushPop(inputLine, commandType):
	resultString = ""
	editedString = ""
	if commandType == "C_PUSH":
		#editedString =
		#resultString
		return
	elif commandType == "C_POP":
		return
	return resultString


#########################################
############ Testing Area ###############
#########################################


def writeHackToFile(inputLineList):
    file = open("test.asm", "w")
    writeString = ""
    for line in inputLineList:
        writeString += line + "\n"
        #writeString += str(line)
    file.write(writeString)
    file.close()


vmToASM()
