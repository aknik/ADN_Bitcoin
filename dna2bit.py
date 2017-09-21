#!/usr/bin/python3

from bitcoin import *
   
def hex2adn(string):

    B = ''.join(['{:>04b}'.format(int(d, 16)) for d in string[0:]])
    #print (B)
    return ''.join('ATCG'[int(B[i:i+2],2)] for i in range(len(B))[::2])

def adn2hex(A):
    B = A.translate(str.maketrans("ATCG","0123"))
    #print (B)
    return hex(int( B, 4))[2:]

ceros = "0000000000000000000000000000000000000000000000000000000000000000"
file = open("chromosomex.fa","r")
basura =(file.readline())

while True:
	
    resto = ""
    otras = ""
   
    letra =(file.read(1))
    if (letra =='A')or(letra =='T')or(letra =='C')or(letra =='G'): 
        while len(resto)<127:
            otras = file.read(1)
        
            if (otras =='A')or(otras =='T')or(otras =='C')or(otras =='G'): resto = resto + otras
                      
        address = letra+resto
        print (address) 
        hexad = (adn2hex(address))
        print (len(hexad))
        hexad = (ceros[:64-len(hexad)] + hexad)     
        print (privtoaddr(hexad))
        #input("Press Enter to continue...")
        
