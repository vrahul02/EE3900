import numpy as np
import matplotlib.pyplot as plt
from sympy.matrices import Matrix

# Generate line points
def line_gen(A,B):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

# Input points
A=np.array([3,1])
B=np.array([6,4])
C=np.array([8,6])

# Printing input
print("A:\n ",A)
print("B:\n ",B)
print("C:\n ",C)

# Making the M matrix
M=Matrix([B-A,C-A])

# Verifing M with what was calculated in tex file
print(M)

# Taking rref of M matrix
M_rref = M.rref()
print("The reff of matrix M is given as : ",M_rref)

# Calculating the rank of Matrix M (here M and N respresent same matrix)
N=np.array([B-A,C-A])
print("rank of matrix = ",np.linalg.matrix_rank(N))
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)

# Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')

# Plotting the points
plt.plot(A[0], A[1], 'o')
plt.text(A[0], A[1] * (1 + 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 + 0.05), B[1] * (1) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0]*(1+0.05), C[1] * (1 - 0.05) , 'C')
plt.grid()
plt.xlim(1,10)
plt.ylim(-2,8)
plt.legend(loc='lower right')
plt.xlabel('x')
plt.ylabel('y')
plt.show()