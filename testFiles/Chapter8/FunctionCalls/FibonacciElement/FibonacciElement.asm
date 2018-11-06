@256
D=A
@0
M=D
@1
D=A
@R2
M=D+M
A=M
D=M
@R0
M=M+1
A=M-1
M=D
@1
D=-A
@R2
M=D+M		//push argument 1
@R0
M=M-1
A=M
D=M
@4
M=D		//pop pointer 1		//pop pointer 1
@0
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 0
@0
D=A
@R4
M=D+M
@R0
M=M-1
A=M
D=M
@R4
A=M
M=D
@0
D=-A
@R4
M=D+M		//pop that 0
@1
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 1
@1
D=A
@R4
M=D+M
@R0
M=M-1
A=M
D=M
@R4
A=M
M=D
@1
D=-A
@R4
M=D+M		//pop that 1
@0
D=A
@R2
M=D+M
A=M
D=M
@R0
M=M+1
A=M-1
M=D
@0
D=-A
@R2
M=D+M		//push argument 0
@2
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 2
@R0
M=M-1
A=M-1
D=M
A=A+1
D=D-M
A=A-1
M=D		//sub
@0
D=A
@R2
M=D+M
@R0
M=M-1
A=M
D=M
@R2
A=M
M=D
@0
D=-A
@R2
M=D+M		//pop argument 0
(MAIN_LOOP_START)	//label MAIN_LOOP_START
@0
D=A
@R2
M=D+M
A=M
D=M
@R0
M=M+1
A=M-1
M=D
@0
D=-A
@R2
M=D+M		//push argument 0
@R0
M=M-1
A=M
D=M
@COMPUTE_ELEMENT
D;JNE	//if-goto COMPUTE_ELEMENT
@ND_PROGRAM
D;JMP	//goto END_PROGRAM
(COMPUTE_ELEMENT)	//label COMPUTE_ELEMENT
@0
D=A
@R4
M=D+M
A=M
D=M
@R0
M=M+1
A=M-1
M=D
@0
D=-A
@R4
M=D+M		//push that 0
@1
D=A
@R4
M=D+M
A=M
D=M
@R0
M=M+1
A=M-1
M=D
@1
D=-A
@R4
M=D+M		//push that 1
@R0
M=M-1
A=M
D=M
A=A-1
M=D+M	//add
@2
D=A
@R4
M=D+M
@R0
M=M-1
A=M
D=M
@R4
A=M
M=D
@2
D=-A
@R4
M=D+M		//pop that 2
@4
D=M
@R0
M=M+1
A=M-1
M=D		//push pointer 1
@1
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 1
@R0
M=M-1
A=M
D=M
A=A-1
M=D+M	//add
@R0
M=M-1
A=M
D=M
@4
M=D		//pop pointer 1		//pop pointer 1
@0
D=A
@R2
M=D+M
A=M
D=M
@R0
M=M+1
A=M-1
M=D
@0
D=-A
@R2
M=D+M		//push argument 0
@1
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 1
@R0
M=M-1
A=M-1
D=M
A=A+1
D=D-M
A=A-1
M=D		//sub
@0
D=A
@R2
M=D+M
@R0
M=M-1
A=M
D=M
@R2
A=M
M=D
@0
D=-A
@R2
M=D+M		//pop argument 0
@AIN_LOOP_START
D;JMP	//goto MAIN_LOOP_START
(END_PROGRAM)	//label END_PROGRAM
