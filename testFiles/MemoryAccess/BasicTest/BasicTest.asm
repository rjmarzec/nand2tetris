@10
D=A
@SP
M=M+1
A=M-1
M=D		//push constant 10
temp pop result code
@21
D=A
@SP
M=M+1
A=M-1
M=D		//push constant 21
@22
D=A
@SP
M=M+1
A=M-1
M=D		//push constant 22
temp pop result code
temp pop result code
@36
D=A
@SP
M=M+1
A=M-1
M=D		//push constant 36
temp pop result code
@42
D=A
@SP
M=M+1
A=M-1
M=D		//push constant 42
@45
D=A
@SP
M=M+1
A=M-1
M=D		//push constant 45
temp pop result code
temp pop result code
@510
D=A
@SP
M=M+1
A=M-1
M=D		//push constant 510
temp pop result code
@local 0
D=A
@LCL
M=M+1
A=M-1
M=D		//push local 0
@that 5
D=A
@THAT
M=M+1
A=M-1
M=D		//push that 5
@SP
M=M-1
A=M
D=M
A=A-1
M=D+M	//add
@argument 1
D=A
@ARG
M=M+1
A=M-1
M=D		//push argument 1
tempSubText
@this 6
D=A
@THIS
M=M+1
A=M-1
M=D		//push this 6
@this 6
D=A
@THIS
M=M+1
A=M-1
M=D		//push this 6
@SP
M=M-1
A=M
D=M
A=A-1
M=D+M	//add
tempSubText
@ERROR: Did not find pointer type
D=A
@ERROR: failure when finding pointer segment type
M=M+1
A=M-1
M=D		//push temp 6
@SP
M=M-1
A=M
D=M
A=A-1
M=D+M	//add
