uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#Things to do: 
# - make the split text work for spaces as well
# - debug key square for i/j


def remove_duplicates(string):
    t = ""
    for i in string:
        if i in t:
            pass
        else:
            t = t + i
            
    return t


#split text into groups of two, adds x after if the # of letters is odd
def split_text(text):
    text = text.upper()
    new_text = [list(text[letter:letter+2]) for letter in range(0,len(text),2)]

    for group in new_text:
        if len(group) == 1:
            group.append('x')
    return new_text

#creates a key square based on keyword
def create_key_square(key):
    table = [[],[],[],[],[]]
    has_i_j = False
    current_row = 0

    for letter in remove_duplicates(key): 
        if letter == 'I' or letter == 'J':
            has_i_j = True

        table[current_row].append(letter)
    
    for letter in uppercase:

        if len(table[current_row]) == 5:
            current_row += 1
            if current_row == 5:
                return table

        if letter not in key: 
            if letter == 'I' or letter == 'J':
                if has_i_j == False:
                    table[current_row].append(letter)
                
            else:
                table[current_row].append(letter)

    return table

def encrypt_pair(table,pair):
    letter1 = get_coord(table,pair[0])
    letter2 = get_coord(table,pair[1])

    if letter1[0] == letter2[0]:
        return 'same row'
    if letter1[1] == letter2[1]:
        return 'same column'
    else: 
        return 'rectangle'
        
#gets the row and column of a letter in a playfair table
def get_coord(table,letter):
    for row in table: 
        for column in row:
            if letter == column: 
                return [table.index(row),table[table.index(row)].index(column)]         



table = create_key_square('JOHH') 
print(table)  
print(remove_duplicates('Hello world'))   
#print(get_coord(table,'Z'))
#print(encrypt_pair(table,['J','C']))
#print(create_key_square('IOHN'))
#print(split_text('HelloWorld'))

