@2
D=A
@15
M=M+1
A=M-1
M=D		//push constant 2
@3
D=A
@15
M=M+1
A=M-1
M=D		//push constant 3
@15
M=M-1
A=M
D=M
A=A-1
D=D-M
@EQJUMP0
D;JNE
M=-1
@EQFINISH0
0;JMP
(EQJUMP0)
M=0
(EQFINISH0)	//eq
