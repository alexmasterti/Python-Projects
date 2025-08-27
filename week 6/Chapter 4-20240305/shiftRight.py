#Implementation of shiftRight method
#which shifts the bits in its input one
#place to the Right

def shiftRight(bitstring):

    bitstring = bitstring[len(bitstring)-1] + bitstring[0:len(bitstring)-1]
    
    #return as bit string format
    return bitstring

#get the input form the user
bits = input("Enter string of bits:")

#call the shiftRight method which returns the value
#that is stored in shiftRight

leftRight = shiftRight(bits)

#display the output
print()
print(leftRight)
print()
