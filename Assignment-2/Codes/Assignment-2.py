import numpy as np

# Input matrices
A = np.array([[1,1,-1],[2,0,3],[3,-1,2]])
B = np.array([[1,3],[0,2],[-1,4]])
C = np.array([[1,2,3,-4],[2,0,-2,1]])

print('A =\n',A)
print('B =\n',B)
print('C =\n',C)

# Matrix multiplication
AB = A@B
BC = B@C

# Finding LHS and RHS
LHS = (AB)@C
RHS = A@(BC)

# Printing results
print('(AB)C =',LHS)
print('A(BC) =',RHS)

print('Hence, (AB)C = A(BC)')