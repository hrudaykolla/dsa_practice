def palindrome(s):
    i = 0
    length = len(s)
    l = length-1 
    while i <= l:
        if s[i] != s[l]:
            return False
        i += 1
        l -= 1
    return True

def subString(s):
    for sub_string_length in range(len(s),0,-1):
        print(sub_string_length)
        for no_of_sub_string in range(len(s)-sub_string_length+1):
            sub_string = s[no_of_sub_string : no_of_sub_string+sub_string_length]
            print(f'{sub_string}, palindrome {palindrome(sub_string)}')
            # if palindrome(sub_string):
            #     return sub_string

print(subString('babad'))