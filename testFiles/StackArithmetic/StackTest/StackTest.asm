@16
D=A
@0
M=D

@17
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 17
@17
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 17
@R0
M=M-1
A=M
D=M
A=A-1
D=D-M
@EQJUMP0
D;JNE
@R0
A=M-1
M=-1
@EQFINISH0
0;JMP
(EQJUMP0)
@R0
A=M-1
M=0
(EQFINISH0)	//eq
@17
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 17
@16
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 16
@R0
M=M-1
A=M
D=M
A=A-1
D=D-M
@EQJUMP1
D;JNE
@R0
A=M-1
M=-1
@EQFINISH1
0;JMP
(EQJUMP1)
@R0
A=M-1
M=0
(EQFINISH1)	//eq
@16
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 16
@17
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 17
@R0
M=M-1
A=M
D=M
A=A-1
D=D-M
@EQJUMP2
D;JNE
@R0
A=M-1
M=-1
@EQFINISH2
0;JMP
(EQJUMP2)
@R0
A=M-1
M=0
(EQFINISH2)	//eq
@892
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 892
@891
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 891
@R0
M=M-1
A=M
D=M
A=A-1
D=D-M
@LTJUMP3
D;JLE
@R0
A=M-1
M=-1
@LTFINISH3
0;JMP
(LTJUMP3)
@R0
A=M-1
M=0
(LTFINISH3)	//lt
@891
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 891
@892
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 892
@R0
M=M-1
A=M
D=M
A=A-1
D=D-M
@LTJUMP4
D;JLE
@R0
A=M-1
M=-1
@LTFINISH4
0;JMP
(LTJUMP4)
@R0
A=M-1
M=0
(LTFINISH4)	//lt
@891
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 891
@891
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 891
@R0
M=M-1
A=M
D=M
A=A-1
D=D-M
@LTJUMP5
D;JLE
@R0
A=M-1
M=-1
@LTFINISH5
0;JMP
(LTJUMP5)
@R0
A=M-1
M=0
(LTFINISH5)	//lt
@32767
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 32767
@32766
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 32766
@R0
M=M-1
A=M
D=M
A=A-1
D=D-M
@GTJUMP6
D;JGE
@R0
A=M-1
M=-1
@GTFINISH6
0;JMP
(GTJUMP6)
@R0
A=M-1
M=0
(GTFINISH6)	//gt
@32766
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 32766
@32767
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 32767
@R0
M=M-1
A=M
D=M
A=A-1
D=D-M
@GTJUMP7
D;JGE
@R0
A=M-1
M=-1
@GTFINISH7
0;JMP
(GTJUMP7)
@R0
A=M-1
M=0
(GTFINISH7)	//gt
@32766
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 32766
@32766
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 32766
@R0
M=M-1
A=M
D=M
A=A-1
D=D-M
@GTJUMP8
D;JGE
@R0
A=M-1
M=-1
@GTFINISH8
0;JMP
(GTJUMP8)
@R0
A=M-1
M=0
(GTFINISH8)	//gt
@57
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 57
@31
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 31
@53
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 53
@R0
M=M-1
A=M
D=M
A=A-1
M=D+M	//add
@112
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 112
@R0
M=M-1
A=M-1
D=M
A=A+1
D=D-M
A=A-1
M=D		//sub
@R0
A=M-1
M=-M		//neg
@R0
M=M-1
A=M
D=M
A=A-1
M=D&M	//and
@82
D=A
@R0
M=M+1
A=M-1
M=D		//push constant 82
@R0
M=M-1
A=M
D=M
A=A-1
M=D|M	//or
@R0
A=M-1
D=M
M=!D	//not
