# in python :
# String
# a= "I Love Python"
# O/p "Python Love I"

a = "I Love Python"
words = a.split()
reverse_a = []

for i in range(len(words)-1, -1, -1):
    reverse_a.append(words[i])

print(reverse_a)
print(" ".join(reverse_a))