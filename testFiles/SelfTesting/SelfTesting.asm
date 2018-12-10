(SimpleFunction.test)
@R0
M=M+1
A=M-1
M=0
@R0
M=M+1
A=M-1
M=0		//function SimpleFunction.test 2
@0
D=A
@R1
M=D+M
A=M
D=M
@R0
M=M+1
A=M-1
M=D
@0
D=-A
@R1
M=D+M		//push local 0
@1
D=A
@R1
M=D+M
A=M
D=M
@R0
M=M+1
A=M-1
M=D
@1
D=-A
@R1
M=D+M		//push local 1
@R0
M=M-1
A=M
D=M
A=A-1
M=D+M	//add
@R0
A=M-1
D=M
M=!D	//not
@0
D=A
@R2
A=D+M
D=M
@R0
M=M+1
A=M-1
M=D		//push argument 0
@R0
M=M-1
A=M
D=M
A=A-1
M=D+M	//add
@1
D=A
@R2
A=D+M
D=M
@R0
M=M+1
A=M-1
M=D		//push argument 1
@R0
M=M-1
A=M-1
D=M
A=A+1
D=D-M
A=A-1
M=D		//sub
