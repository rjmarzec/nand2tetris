@10
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 10
@R1	//LCL
M=M-1
A=A+1
D=M
@Rlocal 0
M=D		//pop local 0
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
@R2	//ARG
M=M-1
A=A+1
D=M
@Rargument 2
M=D		//pop argument 2
@R2	//ARG
M=M-1
A=A+1
D=M
@Rargument 1
M=D		//pop argument 1
@36
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 36
@R3	//THIS
M=M-1
A=A+1
D=M
@Rthis 6
M=D		//pop this 6
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
@R4	//THAT
M=M-1
A=A+1
D=M
@Rthat 5
M=D		//pop that 5
@R4	//THAT
M=M-1
A=A+1
D=M
@Rthat 2
M=D		//pop that 2
@510
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 510
@ERROR: register for pointer type not found	//ERROR: could not find pointer type
M=M-1
A=A+1
D=M
@RERROR: could not find pointer type
M=D		//pop temp 6
@local 0
D=A
@R1
M=M+1
A=M-1
M=D		//push local 0
@that 5
D=A
@R4
M=M+1
A=M-1
M=D		//push that 5
@R0
M=M-1
A=M
D=M
A=A-1
M=D+M	//add
@argument 1
D=A
@R2
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
@this 6
D=A
@R3
M=M+1
A=M-1
M=D		//push this 6
@this 6
D=A
@R3
M=M+1
A=M-1
M=D		//push this 6
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
@ERROR: could not find pointer type
D=A
@ERROR: register for pointer type not found
M=M+1
A=M-1
M=D		//push temp 6
@R0
M=M-1
A=M
D=M
A=A-1
M=D+M	//add
