def check_repeat(a,b):

    string_list = a.split(' ')
    temp = []

    for i in string_list:

        if b == i:
            temp.append(b)

    return len(temp)


str_val = input('Enter the  string to check repetition\t:')
word_val = input('Enter the word to check\t:')

print('repetition of word ',word_val,check_repeat(str_val,word_val))



