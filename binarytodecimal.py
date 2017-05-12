# To choose a converter you need to write the function decimal(num) or binary(num)


# DECIMAL SIDE
def decimal(decimalin):

    rest ="" #needed to work
    while True:
        rest += str(decimalin % 2)
        decimalin = decimalin // 2

        if decimalin == 0:
            break

    return rest[::-1]


# BINARY SIDE

def binary(binaryin):
    binaryin = str(binaryin)
    i=0
    i = len(binaryin) -1
    binarynum = 0
    binarydecimal = 0
    binaryintra = ""
    #
    # The next While turns arround the input
    # Example: if you introduce a 1010 to make easy to use the string and numbers
    # I rotate it to 0101 trying to learn how to make it less botched XDDD
    #
    while i>= 0:
        binaryintra = binaryintra + binaryin[i]
        i = i -1
    #
    # Here I made the binary to decimal, as you can see i use the normal used formula
    # (1, 0) * 2^X 
    # X is for the possision of the binary number
    while not binarynum == len(binaryin):
        
##        print(binarynum)        #test
        binarydecimal1=int(binaryintra[binarynum])*2**binarynum
##        print(binarydecimal1) #test
        binarydecimal=binarydecimal+binarydecimal1
        binarynum = binarynum +1
    
    return binarydecimal
