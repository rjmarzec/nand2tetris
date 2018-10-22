@5
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 5
@R0
M=M-1
A=M
D=M
@3
M=D		//pop pointer 0
@6
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 6
@R0
M=M-1
A=M
D=M
@4
M=D		//pop pointer 1
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
