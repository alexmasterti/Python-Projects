#Implementation of Shifleft method
#which shifts the bits in its input one
#place to the left

def shiftLeft(bitstring):

    bitstring = bitstring[2:]+ bitstring[:2]
    
    #return as bit string format
    return bitstring

#get the input form the user
bits = input("Enter string of bits:")

#call the ShiftLeft method which returns the value
#that is stored in leftShift

leftShift = shiftLeft(bits)

#display the output
print()
print(leftShift)
print()
