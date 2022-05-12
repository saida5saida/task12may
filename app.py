#sual 1 
sentence = input("Cumle daxil edin: ")
binary_sentence = ''
for c in sentence:
    if c.isalpha():
        l = bin(ord(c))
        short = l.lstrip("0b")
        binary_sentence += short + ' '
    elif c.isdigit():
        short = l.lstrip("0b")
        binary_sentence += short
#print(binary_sentence)

#sual 2
inp = ("color: rgb(127, 255, 12)")
colors = slice(11, -1)
l = inp[colors]
dvded = l.split(', ')
print(dvded)
hex_version = ''
for n in dvded:
    new_num = hex(int(n))
    shortened = new_num.lstrip("0x")
    hex_version += shortened
#print(hex_version)


