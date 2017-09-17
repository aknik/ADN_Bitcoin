#!/usr/bin/python3

   
def hex2adn(string):
	
    B = ''.join(['{:>04b}'.format(int(d, 16)) for d in string[0:]])
    #print (B)
    return ''.join('ATCG'[int(B[i:i+2],2)] for i in range(len(B))[::2])
   
    
def adn2hex(A):
    B = A.translate(str.maketrans("ATCG","0123"))
    #print (B)
    return hex(int( B, 4))[2:]
    
  
A = "e9873d79c6d87dc0fb6a5778633389f4453213303da61f20bd67fc233aa33262"
print (A)
print (hex2adn(A))


A = "GCCTCATGAGGTTGCTGATCGTCATGGTGAAAGGCGTCCCTTTGTGCATCAGAGAGCACTGGTATATTAGACATAGAGAAAGGTCCTCATGGACAACGGTTCTGGGGAACAGAGCCCCAGAGACTCAC"
print (A)
print (adn2hex(A))

