
"""
infile = open ("Test.txt", 'r')
for line in infile:
    List = line.split();
    print(List)
    for word in List:
        if len(word) == 4:
            print(word)

   
    
"""
Q2 PROJ5 cHAP4 # encrypts an input message using the caesar cypher with a user-defined distance value 



plainText = input("Enter a lowercase message:")
distance = int(input("Enter the distance of encryption:"))

code = ""

for ch in plainText:
  ordValue = ord(ch)
  if ordValue > 60 and ordValue < 123:
    cipherValue = ordValue + distance
    if cipherValue > ord("z"):
       cipherValue = ord("a") + distance - (ord("z") - ordValue + 1)
    code += chr(cipherValue)
  else:
    code += ch
print(code)

