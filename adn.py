# python3

    
def hex2adn(string):
	
    B = ''.join(['{:>04b}'.format(int(d, 16)) for d in string[0:]])
    return ''.join('ATCG'[int(B[i:i+2],2)] for i in range(len(B))[::2])
    
def adn2hex(B):
	
    B = B.replace('A', '0')
    B = B.replace('T', '1')
    B = B.replace('C', '2')
    B = B.replace('G', '3')    
    return hex(int( B, 4))[2:]
    
 
    
A = "e9873d79c6d87dc0fb6a5778633389f4453213303da61f20bd67fc233aa33262"
print (A)
print (hex2adn(A))

A = "GCCTCATGAGGTTGCTGATCGTCATGGTGAAAGGCGTCCCTTTGTGCATCAGAGAGCACTGGTATATTAGACATAGAGAAAGGTCCTCATGGACAACGGTTCTGGGGAACAGAGCCCCAGAGACTCAC"
print (A)
print (adn2hex(A))
