uppercase = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
#Things to do: 
# - decryption method
# - clean up everything

#removes double occurances of a letter in a string (used for keywords and table creation)
def remove_duplicates(string):
    t = ""
    for i in string:
        if i in t:
            pass
        else:
            t = t + i 
    return t

#adds an 'X' inbetween double occurances of letters (hello -> helxlo)
def split_doubles(string):
    new_string = ''
    for i in range (len(string)-1):
        if string[i] == string[i+1]:
            new_string += string[i] + 'X'
        else:
            new_string += string[i]
    return new_string + string[-1]

#split text into groups of two, adds x after if the # of letters is odd
def split_text(text):
    text = split_doubles(text.upper().replace(' ','').replace('J','I'))
    new_text = [list(text[letter:letter+2]) for letter in range(0,len(text),2)]

    for group in new_text:
        if len(group) == 1:
            group.append('X')
    return new_text

#creates a key square based on keyword
def create_key_square(key):
    key = key.replace('J','I').upper()
    table = [[],[],[],[],[]]
    current_row = 0

    for letter in remove_duplicates(key): 
        if len(table[current_row]) == 5:
            current_row += 1
        table[current_row].append(letter)
    
    for letter in uppercase:
        if len(table[current_row]) == 5:
            current_row += 1
            if current_row == 5:
                return table

        if letter not in key: 
            table[current_row].append(letter)

    return table

#function to encrypt each individual pair of text
def encrypt_pair(table,pair):
    letter1 = get_coord(table,pair[0])
    letter2 = get_coord(table,pair[1])

    if letter1[0] == letter2[0]:
        return [table[letter1[0]][(letter1[1]+1)%5],table[letter2[0]][(letter2[1]+1)%5]]
    if letter1[1] == letter2[1]:
        return [table[(letter1[0]+1)%5][letter1[1]],table[(letter2[0]+1)%5][letter2[1]]]
    else: 
        return [table[letter1[0]][letter2[1]],table[letter2[0]][letter1[1]]]

#goes through each pair and encrypts it
def encrypt_text(table,text):
    cipher_text = []
    for pair in text:
        cipher_text.append(encrypt_pair(table,pair))
    return cipher_text

#gets the row and column of a letter in a playfair table
def get_coord(table,letter):
    for row in table: 
        for column in row:
            if letter == column: 
                return [table.index(row),table[table.index(row)].index(column)]

#formats ciphertext in str format
def print_ciphertext(ciphertext):      
    text = ''
    for pair in ciphertext:
        for letter in pair: 
            text += letter
        text += ' '
    return text      

keyword = input('Keyword: ')
plaintext = input('Plaintext: ')
table = create_key_square(keyword)
ciphertext = encrypt_text(table,split_text(split_doubles(plaintext)))
print(split_text(plaintext))
print(print_ciphertext(ciphertext))
