a = ['2', '5', '5', '6', '3', '-3', '-9']
b =['4','-5','7','6','3', '0','-8']
c= a+b
print(c)
d=[]

for i in c:
    if i not in d :
        d.append(i)
print(d)
e =[int(i) for i in d]
print(e)
for i in range(len(e)):
    for j in range(i + 1, len(e)):
        if e[i] > e[j]:
            e[i], e[j] = e[j], e[i]

print(e)



