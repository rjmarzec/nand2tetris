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
@5
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 5
@10
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 10
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
M=D+M	//pop that 0
@0
D=A
@R3
M=D+M
@R0
M=M-1
A=M
D=M
@R3
A=M
M=D
@0
D=-A
@R3
M=D+M	//pop this 0
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
M=D+M	//push that 0
@0
D=A
@R3
M=D+M
A=M
D=M
@R0
M=M+1
A=M-1
M=D
@0
D=-A
@R3
M=D+M	//push this 0
