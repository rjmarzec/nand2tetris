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
A=A+1
D=M
@R24
M=D		//pop static 8
A=A+1
D=M
@R19
M=D		//pop static 3
A=A+1
D=M
@R17
M=D		//pop static 1
@3
D=A
@ERROR: register for pointer type not found
M=M+1
A=M-1
M=D		//push static 3
@1
D=A
@ERROR: register for pointer type not found
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
@8
D=A
@ERROR: register for pointer type not found
M=M+1
A=M-1
M=D		//push static 8
@R0
M=M-1
A=M
D=M
A=A-1
M=D+M	//add
