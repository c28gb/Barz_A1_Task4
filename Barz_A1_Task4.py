uppercase = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
#Things to do: 
# - make the split text work for spaces as well


def remove_duplicates(string):
    t = ""
    for i in string:
        if i in t:
            pass
        else:
            t = t + i
            
    return t

def remove_doubles(string):
    for i in range (len(string)-1):
        if string[i] == string[i+1]:
            string = string[:i] + 'x' + string[i:]
    return string

#split text into groups of two, adds x after if the # of letters is odd
def split_text(text):
    text = text.upper().replace(' ','')
    text = text.replace('J','I')
    new_text = [list(text[letter:letter+2]) for letter in range(0,len(text),2)]

    for group in new_text:
        if len(group) == 1:
            group.append('X')
    return new_text

#creates a key square based on keyword
def create_key_square(key):
    key = key.replace('J','I')
    table = [[],[],[],[],[]]
    current_row = 0

    for letter in remove_duplicates(key): 
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
         
#print(split_text('Johnny'))
table = create_key_square('HELLO') 
#print(table)  
#print(remove_duplicates('Hello world'))   
#print(get_coord(table,'Z'))
#print(encrypt_pair(table,['H','D']))

#print(create_key_square('IOHN'))
print(split_text('plain exts'))
#print(encrypt_text(table,split_text('plaintexts')))
print(remove_doubles('hello'))
