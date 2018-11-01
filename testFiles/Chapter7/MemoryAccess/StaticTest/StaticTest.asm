@256
D=A
@0
M=D
@111
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 111
@333
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 333
@888
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 888
@R0
M=M-1
A=M
D=M
@24
M=D		//pop static 8
@R0
M=M-1
A=M
D=M
@19
M=D		//pop static 3
@R0
M=M-1
A=M
D=M
@17
M=D		//pop static 1
@19
D=M
@R0
M=M+1
A=M-1
M=D		//push static 3
@17
D=M
@R0
M=M+1
A=M-1
M=D		//push static 1
@R0
M=M-1
A=M-1
D=M
A=A+1
D=D-M
A=A-1
M=D		//sub
@24
D=M
@R0
M=M+1
A=M-1
M=D		//push static 8
@R0
M=M-1
A=M
D=M
A=A-1
M=D+M	//add
