@3030
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 3030
@R0
M=M-1
A=M
D=M
@3
M=D		//pop pointer 0
@3040
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 3040
@R0
M=M-1
A=M
D=M
@4
M=D		//pop pointer 1
@32
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 32
@2
D=A
@R3
M=D+M
@R0
M=M-1
A=M+1
D=M
@R3
A=M
M=D
@2
D=-A
@R3
M=D+M	//pop this 2
@46
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 46
@6
D=A
@R4
M=D+M
@R0
M=M-1
A=M+1
D=M
@R4
A=M
M=D
@6
D=-A
@R4
M=D+M	//pop that 6
@3
D=M
@R0
M=M+1
A=M-1
M=D		//push pointer 0
@4
D=M
@R0
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
M=D+M
A=M
D=M
@R0
M=M+1
A=M-1
M=D
@2
D=-A
@R3
M=D+M	//push this 2
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
M=D+M
A=M
D=M
@R0
M=M+1
A=M-1
M=D
@6
D=-A
@R4
M=D+M	//push that 6
@R0
M=M-1
A=M
D=M
A=A-1
M=D+M	//add
