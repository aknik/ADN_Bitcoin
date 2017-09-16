# python3

def f(A):
    g = ''.join 
    B = bin(int(g(map(str,map(ord,A)))))[2:] # convert string input to binary
    B += len(B)%2 * '0' # add extra 0 if necessary
    B = "10000111001111010111100111000110110110000111110111000000111110110110101001010111011110000110001100110011100010011111010001000101001100100001001100110000001111011010011000011111001000001011110101100111111111000010001100111010101000110011001001100010"
    
    return g('ACGT'[int(B[i:i+2],2)] for i in range(len(B))[::2]) # map every two characters into 'ACGT
    
def adn(string):
	
    B = ''.join(['{:>04b}'.format(int(d, 16)) for d in string[2:]])
    print (B)
    return ''.join ('ACGT'[int(B[i:i+2],2)] for i in range(len(B))[::2])
    
    
print (f('E9873D79C6D87DC0FB6A5778633389F4453213303DA61F20BD67FC233AA33262'))

print (adn('E9873D79C6D87DC0FB6A5778633389F4453213303DA61F20BD67FC233AA33262'))
