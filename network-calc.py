def Network_calc():
    ipin = str(input("enter a ip"))
    ipcount = ipin.count(".")
    if not ipcount == 3:
        print("not a valid ip")
        exit
    maskin = input("enter a mask" )
    maskcount = maskin.count(".")
    if not maskcount == 3:
        print("not a valid ip")
    ip1 = ipin.find(".")
    ip1ok=int(ipin[:(ip1)])
    print(ip1ok)
    ip2 =(ipin[(ip1+1):].find("."))

    ip2ok = int(ipin[(ip1+1):ip1+1+ip2])
    print(ip2ok)

    ip3 = ipin[(ip1+1+ip2+1):].find(".")
    ip3ok= int(ipin[(ip1+1+ip2+1):ip1+1+ip2+1+ip3])
    print(ip3ok)

    ip4ok = int(ipin[(ip1+1+ip2+1+ip3+1):len(ipin)])
    print(ip4ok)


    mask1 = maskin.find(".")
    mask1ok=int(maskin[:(mask1)])
    print(mask1ok)
    mask2 =(maskin[(mask1+1):].find("."))

    mask2ok = int(maskin[(mask1+1):mask1+1+mask2])
    print(mask2ok)

    mask3 = maskin[(mask1+1+mask2+1):].find(".")
    mask3ok= int(maskin[(mask1+1+mask2+1):mask1+1+mask2+1+mask3])
    print(mask3ok)

    mask4ok =int( maskin[(mask1+1+mask2+1+mask3+1):len(maskin)])
    print(mask4ok)
    print("#############################BINARY###########################")
    print("Ip")
    print(bin(ip1ok))
    print(bin(ip2ok))
    print(bin(ip3ok))
    print(bin(ip4ok))
    print("mask")
    print(bin(mask1ok))
    print(bin(mask2ok))
    print(bin(mask3ok))
    print(bin(mask4ok))
    
