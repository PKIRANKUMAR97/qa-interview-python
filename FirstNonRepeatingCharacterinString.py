str = "automtiontestinwithpythonseleniumpytest"
freq = {}
for char in str:
    freq[char]=freq.get(char,0)+1
for char in str:
    if freq[char]==1:
        print("first non reapeating character is : ",char)
        break
print(freq)