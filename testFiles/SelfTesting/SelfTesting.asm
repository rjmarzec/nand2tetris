@16
D=A
@0
M=D
(SelfTesting.func)
@R0
M=M+1
A=M-1
M=0
@R0
M=M+1
A=M-1
M=0
@R0
M=M+1
A=M-1
M=0	//function SelfTesting.func 3
@10
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 10
@10
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 10
@R0
M=M-1
A=M
D=M
A=A-1
M=D+M	//add
