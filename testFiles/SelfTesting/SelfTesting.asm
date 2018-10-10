@2
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 2
@3
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 3
@R0
M=M-1
A=M
D=M
A=A-1
D=D-M
@GTJUMP0
D;JGT
@R0
A=M-1
M=-1
@GTFINISH0
0;JMP
(GTJUMP0)
@R0
A=M-1
M=0
(GTFINISH0)	//gt
