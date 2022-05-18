def swapFileData ():
    input("a.txt")
    input("b.txt")
    with open(a,'r') as a:
        data_a=a.read()

    with open(a,'w') as a:
        a.write(data_b)
    
swapFileData()    