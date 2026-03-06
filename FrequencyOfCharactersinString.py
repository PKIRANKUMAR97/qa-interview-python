def fun_frequencyofcharactersinstring(s):
    frequency = {}
    for char in s:
        if char not in frequency:
            frequency[char] = 1
        else:
            frequency[char] = frequency[char] + 1
    return frequency

print(fun_frequencyofcharactersinstring("abcdabcd"))

"""
def fun(s):
    freq={}
    for char in s:
        freq[char]=freq.get(char,0)+1
        
    return freq
    
print(fun("acdsfcdsacdsca"))


"""