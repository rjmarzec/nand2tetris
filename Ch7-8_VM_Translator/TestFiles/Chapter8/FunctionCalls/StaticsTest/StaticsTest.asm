@256
D=A
@0
M=D
@RETURNADDRESS0
D=A
@R0
M=M+1
A=M-1
M=D
@R1
D=M
@R0
M=M+1
A=M-1
M=D
@R2
D=M
@R0
M=M+1
A=M-1
M=D
@R3
D=M
@R0
M=M+1
A=M-1
M=D
@R4
D=M
@R0
M=M+1
A=M-1
M=D
@R0
D=M
@0
D=D-A
@5
D=D-A
@R2
M=D
@R0
D=M
@R1
M=D
@Sys.init
0;JMP
(RETURNADDRESS0)	//call Sys.init 0

(LOOP)	//label LOOP

@LOOP
0;JMP	//goto LOOP

(Sys.init)		//function Sys.init 0

@6
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 6

@8
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 8

@RETURNADDRESS1
D=A
@R0
M=M+1
A=M-1
M=D
@R1
D=M
@R0
M=M+1
A=M-1
M=D
@R2
D=M
@R0
M=M+1
A=M-1
M=D
@R3
D=M
@R0
M=M+1
A=M-1
M=D
@R4
D=M
@R0
M=M+1
A=M-1
M=D
@R0
D=M
@2
D=D-A
@5
D=D-A
@R2
M=D
@R0
D=M
@R1
M=D
@Class1.set
0;JMP
(RETURNADDRESS1)	//call Class1.set 2

@R0
M=M-1
A=M
D=M
@5
M=D		//pop temp 0

@23
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 23

@15
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 15

@RETURNADDRESS2
D=A
@R0
M=M+1
A=M-1
M=D
@R1
D=M
@R0
M=M+1
A=M-1
M=D
@R2
D=M
@R0
M=M+1
A=M-1
M=D
@R3
D=M
@R0
M=M+1
A=M-1
M=D
@R4
D=M
@R0
M=M+1
A=M-1
M=D
@R0
D=M
@2
D=D-A
@5
D=D-A
@R2
M=D
@R0
D=M
@R1
M=D
@Class2.set
0;JMP
(RETURNADDRESS2)	//call Class2.set 2

@R0
M=M-1
A=M
D=M
@5
M=D		//pop temp 0

@RETURNADDRESS3
D=A
@R0
M=M+1
A=M-1
M=D
@R1
D=M
@R0
M=M+1
A=M-1
M=D
@R2
D=M
@R0
M=M+1
A=M-1
M=D
@R3
D=M
@R0
M=M+1
A=M-1
M=D
@R4
D=M
@R0
M=M+1
A=M-1
M=D
@R0
D=M
@0
D=D-A
@5
D=D-A
@R2
M=D
@R0
D=M
@R1
M=D
@Class1.get
0;JMP
(RETURNADDRESS3)	//call Class1.get 0

@RETURNADDRESS4
D=A
@R0
M=M+1
A=M-1
M=D
@R1
D=M
@R0
M=M+1
A=M-1
M=D
@R2
D=M
@R0
M=M+1
A=M-1
M=D
@R3
D=M
@R0
M=M+1
A=M-1
M=D
@R4
D=M
@R0
M=M+1
A=M-1
M=D
@R0
D=M
@0
D=D-A
@5
D=D-A
@R2
M=D
@R0
D=M
@R1
M=D
@Class2.get
0;JMP
(RETURNADDRESS4)	//call Class2.get 0

(WHILE)	//label WHILE

@WHILE
0;JMP	//goto WHILE

(Class1.set)		//function Class1.set 0

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
@16
M=D		//pop static 0

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
A=M
D=M
@17
M=D		//pop static 1

@0
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 0

@R1
D=M
@13
M=D
@13
D=M
@5
D=D-A
A=D
D=M
@14
M=D
@R0
M=M-1
A=M
D=M
@R2
A=M
M=D
@R2
D=M+1
@R0
M=D
@13
D=M
@1
D=D-A
A=D
D=M
@R4
M=D
@13
D=M
@2
D=D-A
A=D
D=M
@R3
M=D
@13
D=M
@3
D=D-A
A=D
D=M
@R2
M=D
@13
D=M
@4
D=D-A
A=D
D=M
@R1
M=D
@14
A=M
0;JMP		//return

(Class1.get)		//function Class1.get 0

@16
D=M
@R0
M=M+1
A=M-1
M=D		//push static 0

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

@R1
D=M
@13
M=D
@13
D=M
@5
D=D-A
A=D
D=M
@14
M=D
@R0
M=M-1
A=M
D=M
@R2
A=M
M=D
@R2
D=M+1
@R0
M=D
@13
D=M
@1
D=D-A
A=D
D=M
@R4
M=D
@13
D=M
@2
D=D-A
A=D
D=M
@R3
M=D
@13
D=M
@3
D=D-A
A=D
D=M
@R2
M=D
@13
D=M
@4
D=D-A
A=D
D=M
@R1
M=D
@14
A=M
0;JMP		//return

(Class2.set)		//function Class2.set 0

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
@18
M=D		//pop static 2

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
A=M
D=M
@19
M=D		//pop static 3

@0
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 0

@R1
D=M
@13
M=D
@13
D=M
@5
D=D-A
A=D
D=M
@14
M=D
@R0
M=M-1
A=M
D=M
@R2
A=M
M=D
@R2
D=M+1
@R0
M=D
@13
D=M
@1
D=D-A
A=D
D=M
@R4
M=D
@13
D=M
@2
D=D-A
A=D
D=M
@R3
M=D
@13
D=M
@3
D=D-A
A=D
D=M
@R2
M=D
@13
D=M
@4
D=D-A
A=D
D=M
@R1
M=D
@14
A=M
0;JMP		//return

(Class2.get)		//function Class2.get 0

@18
D=M
@R0
M=M+1
A=M-1
M=D		//push static 2

@19
D=M
@R0
M=M+1
A=M-1
M=D		//push static 3

@R0
M=M-1
A=M-1
D=M
A=A+1
D=D-M
A=A-1
M=D		//sub

@R1
D=M
@13
M=D
@13
D=M
@5
D=D-A
A=D
D=M
@14
M=D
@R0
M=M-1
A=M
D=M
@R2
A=M
M=D
@R2
D=M+1
@R0
M=D
@13
D=M
@1
D=D-A
A=D
D=M
@R4
M=D
@13
D=M
@2
D=D-A
A=D
D=M
@R3
M=D
@13
D=M
@3
D=D-A
A=D
D=M
@R2
M=D
@13
D=M
@4
D=D-A
A=D
D=M
@R1
M=D
@14
A=M
0;JMP		//return

