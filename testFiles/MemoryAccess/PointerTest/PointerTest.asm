@3030
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 3030
@R3
M=M-1
A=A+1
D=M
@R0
M=D		//pop pointer 0
@3040
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 3040
@R3
M=M-1
A=A+1
D=M
@R1
M=D		//pop pointer 1
@32
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 32
@R3
M=M-1
A=A+1
D=M
@R2
M=D		//pop this 2
@46
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 46
@R4
M=M-1
A=A+1
D=M
@R6
M=D		//pop that 6
@0
D=A
@R3
M=M+1
A=M-1
M=D		//push pointer 0
@1
D=A
@R3
M=M+1
A=M-1
M=D		//push pointer 1
@R0
M=M-1
A=M
D=M
A=A-1
M=D+M	//add
@2
D=A
@R3
M=M+1
A=M-1
M=D		//push this 2
@R0
M=M-1
A=M-1
D=M
A=A+1
D=D-M
A=A-1
M=D		//sub
@6
D=A
@R4
M=M+1
A=M-1
M=D		//push that 6
@R0
M=M-1
A=M
D=M
A=A-1
M=D+M	//add
