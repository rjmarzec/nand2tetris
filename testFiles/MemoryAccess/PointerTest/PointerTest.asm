@3030
D=A
@SP
M=M+1
A=M-1
M=D		//push constant 3030
ERROR: could not find pointer type@@@@@@@@@@@@@@@@@@
@3040
D=A
@SP
M=M+1
A=M-1
M=D		//push constant 3040
ERROR: could not find pointer type@@@@@@@@@@@@@@@@@@
@32
D=A
@SP
M=M+1
A=M-1
M=D		//push constant 32
this 2@@@@@@@@@@@@@@@@@@
@46
D=A
@SP
M=M+1
A=M-1
M=D		//push constant 46
that 6@@@@@@@@@@@@@@@@@@
@ERROR: could not find pointer type
D=A
@ERROR: could not find pointer type
M=M+1
A=M-1
M=D		//push pointer 0
@ERROR: could not find pointer type
D=A
@ERROR: could not find pointer type
M=M+1
A=M-1
M=D		//push pointer 1
@SP
M=M-1
A=M
D=M
A=A-1
M=D+M	//add
@this 2
D=A
@THIS
M=M+1
A=M-1
M=D		//push this 2
@SP
M=M-1
A=M
A=A+1
D=M
A=A+1
M=D-M	//sub
@that 6
D=A
@THAT
M=M+1
A=M-1
M=D		//push that 6
@SP
M=M-1
A=M
D=M
A=A-1
M=D+M	//add
