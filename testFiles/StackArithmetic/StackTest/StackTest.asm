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
@LTJUMP7
D;JLE
@R0
A=M-1
M=-1
@LTFINISH7
0;JMP
(LTJUMP7)
@R0
A=M-1
M=0
(LTFINISH7)	//lt
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
@GTJUMP9
D;JGT
@R0
A=M-1
M=-1
@GTFINISH9
0;JMP
(GTJUMP9)
@R0
A=M-1
M=0
(GTFINISH9)	//gt
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
@GTJUMP11
D;JGT
@R0
A=M-1
M=-1
@GTFINISH11
0;JMP
(GTJUMP11)
@R0
A=M-1
M=0
(GTFINISH11)	//gt
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
@GTJUMP13
D;JGT
@R0
A=M-1
M=-1
@GTFINISH13
0;JMP
(GTJUMP13)
@R0
A=M-1
M=0
(GTFINISH13)	//gt
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
M=!M	//not
