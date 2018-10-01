@2
D=A
@15
M=M+1
A=M-1
M=D		//push constant 2
@5
D=A
@15
M=M+1
A=M-1
M=D		//push constant 5

//get the value of the stack pointer
@15
//set the pointer back 1 for our use and later use
M=M-1
//go to the the number we want to be subtracting from
A=M-1
//store said value
D=M
//go back up 1 value to the number we are subtracting
A=A+1
//subtract the 2 numbers and store it
D=D-M   //sub
A=A-1
M=D

