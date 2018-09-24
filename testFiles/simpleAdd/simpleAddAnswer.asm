// Contains the correct version translation of simpleAdd.vm to simpleAdd.asm for my sanity
//Taken from https://github.com/gshaw/nand2tetris/blob/master/07/StackArithmetic/SimpleAdd/SimpleAdd.asm

@7      // push constant 7
D=A
@SP
A=M
M=D
@SP
M=M+1
@8      // push constant 8
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP     // add
D=M
AM=D-1
D=M
A=A-1
M=M+D