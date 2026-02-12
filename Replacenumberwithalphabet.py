

l1=[10,55,76,45,76]

def repl(l1):

    l2=[]
    for i in l1:
        j=str(i).replace("6","a")
        l2.append(j)

    print(l2)

repl(l1)