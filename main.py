file = open('Странное письмо.txt')

text = file.read()  # "1057 1087 1072 1084 32 1089 1087 1072..."
file.close()

file2 = open('rasshifr.txt', 'wt')
str_numbers = text.split()  # ["1057", "1087", "1072", "1084"...]
for str_number in str_numbers:
    number = int(str_number)
    file2.write(chr(number))

file2.close()
