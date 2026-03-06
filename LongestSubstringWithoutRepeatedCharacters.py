def func_LongestSubstring(s):
    max_len = 0
    substring = ""
    for char in s:
        if char not in substring:
            substring = substring + char

        else :
            substring = substring[substring.index(char)+1 : ] + char

        max_len = max(max_len, len(substring))

    return max_len
print(func_LongestSubstring(""))


