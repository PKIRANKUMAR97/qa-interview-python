l1=[91,27,33,49,52,78,90,334,234,897,3344]

def rp2(l1):
    L2=[]
    for i in l1:

        j=str(i).replace("3","A")
        L2.append(j)
    print(L2)

rp2(l1)


