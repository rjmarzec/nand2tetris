@256
D=A
@0
M=D
@10
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 10
@0
D=A
@R1
M=D+M
@R0
M=M-1
A=M
D=M
@R1
A=M
M=D
@0
D=-A
@R1
M=D+M	//pop local 0
@21
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 21
@22
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 22
@2
D=A
@R2
M=D+M
@R0
M=M-1
A=M
D=M
@R2
A=M
M=D
@2
D=-A
@R2
M=D+M	//pop argument 2
@1
D=A
@R2
M=D+M
@R0
M=M-1
A=M
D=M
@R2
A=M
M=D
@1
D=-A
@R2
M=D+M	//pop argument 1
@36
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 36
@6
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
@6
D=-A
@R3
M=D+M	//pop this 6
@42
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 42
@45
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 45
@5
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
@5
D=-A
@R4
M=D+M	//pop that 5
@2
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
@2
D=-A
@R4
M=D+M	//pop that 2
@510
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 510
@R0
M=M-1
A=M
D=M
@11
M=D		//pop temp 6
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
M=D+M	//push local 0
@5
D=A
@R4
M=D+M
A=M
D=M
@R0
M=M+1
A=M-1
M=D
@5
D=-A
@R4
M=D+M	//push that 5
@R0
M=M-1
A=M
D=M
A=A-1
M=D+M	//add
@1
D=A
@R2
M=D+M
A=M
D=M
@R0
M=M+1
A=M-1
M=D
@1
D=-A
@R2
M=D+M	//push argument 1
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
@R3
M=D+M
A=M
D=M
@R0
M=M+1
A=M-1
M=D
@6
D=-A
@R3
M=D+M	//push this 6
@6
D=A
@R3
M=D+M
A=M
D=M
@R0
M=M+1
A=M-1
M=D
@6
D=-A
@R3
M=D+M	//push this 6
@R0
M=M-1
A=M
D=M
A=A-1
M=D+M	//add
@R0
M=M-1
A=M-1
D=M
A=A+1
D=D-M
A=A-1
M=D		//sub
@11
D=M
@R0
M=M+1
A=M-1
M=D		//push temp 6
@R0
M=M-1
A=M
D=M
A=A-1
M=D+M	//add
