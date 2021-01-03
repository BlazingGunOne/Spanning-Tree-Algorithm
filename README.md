# Spanning-Tree-Algorithm
Implement the spanning tree protocol on a given LAN and bridge topology,
and then simulate the functioning of the learning bridges for a sequence of given data
transfers.
You have to write a program that first reads the input, creates some internal
representation of the LAN topology, and then starts with states of a Bridge’s ports as active
on all ports. It should then simulate the running of the spanning tree protocol - thus at t=0 all
bridges will send their advertisements and then as time progresses will behave according to
the protocol. 
Input:
0
7
B1: A G B
B2: G F
B3: B C
B4: C F E
B5: C D E
B6: F E H
B7: H D
Here DP = Designated  Port,  RP = Root Port,  and NP = Null Port (deactivated port).
After this, the program should read a list of host IDs per LAN and a set of data transfer end points which will be specified as follows.
Your program should print out the forwarding tables at each bridge after each data transfer, in the following syntax. 
Input:
A: H1 H2
B: H3 H4
C: H5
D: H6
E: H7
F: H8 H9 H10
G: H11 H12
H: H13 H14
4
H1 H2
H9 H2
H4 H12
H3 H9
Overall Output:
B1: A-DP B-DP G-DP
B2: F-DP G-RP
B3: B-RP C-DP
B4: C-NP E-DP F-RP
B5: C-RP D-DP E-NP
B6: E-NP F-RP H-DP
B7: D-RP H-NP
B1:
HOST ID | FORWARDING PORT
H1 | A
B2:
HOST ID | FORWARDING PORT
H1 | G
B3:
HOST ID | FORWARDING PORT
H1 | B
B4:
HOST ID | FORWARDING PORT
H1 | F
B5:
HOST ID | FORWARDING PORT
H1 | C
B6:
HOST ID | FORWARDING PORT
H1 | F
B7:
HOST ID | FORWARDING PORT
H1 | D

B1:
HOST ID | FORWARDING PORT
H1 | A
H9 | G
B2:
HOST ID | FORWARDING PORT
H1 | G
H9 | F
B3:
HOST ID | FORWARDING PORT
H1 | B
H9 | B
B4:
HOST ID | FORWARDING PORT
H1 | F
H9 | F
B5:
HOST ID | FORWARDING PORT
H1 | C
H9 | C
B6:
HOST ID | FORWARDING PORT
H1 | F
H9 | F
B7:
HOST ID | FORWARDING PORT
H1 | D
H9 | D

B1:
HOST ID | FORWARDING PORT
H1 | A
H4 | B
H9 | G
B2:
HOST ID | FORWARDING PORT
H1 | G
H4 | G
H9 | F
B3:
HOST ID | FORWARDING PORT
H1 | B
H4 | B
H9 | B
B4:
HOST ID | FORWARDING PORT
H1 | F
H4 | F
H9 | F
B5:
HOST ID | FORWARDING PORT
H1 | C
H4 | C
H9 | C
B6:
HOST ID | FORWARDING PORT
H1 | F
H4 | F
H9 | F
B7:
HOST ID | FORWARDING PORT
H1 | D
H4 | D
H9 | D

B1:
HOST ID | FORWARDING PORT
H1 | A
H3 | B
H4 | B
H9 | G
B2:
HOST ID | FORWARDING PORT
H1 | G
H3 | G
H4 | G
H9 | F
B3:
HOST ID | FORWARDING PORT
H1 | B
H3 | B
H4 | B
H9 | B
B4:
HOST ID | FORWARDING PORT
H1 | F
H3 | F
H4 | F
H9 | F
B5:
HOST ID | FORWARDING PORT
H1 | C
H4 | C
H9 | C
B6:
HOST ID | FORWARDING PORT
H1 | F
H3 | F
H4 | F
H9 | F
B7:
HOST ID | FORWARDING PORT
H1 | D
H4 | D
H9 | D
