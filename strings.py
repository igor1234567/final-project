mystring= 'monty pythons flying circus'

def no_duplicates(a_string):
    p= ""
    for char in a_string:
        if char not in p:
            p= p + char
    p= ''.join(sorted(p))
    print(p)
#    return p



def reversed_words(a_string):
    a_string= a_string.split(" ")
    a_string.reverse()
    print(a_string)
#    return a_string

def four_char_strings(a_string):
    n= 4
    chunks= []
    for i in range(0, len(a_string), n):
        chunks.append(a_string[i:i + n])
    print(chunks)
#    return chunks



s='monty pythons flying circus'
no_duplicates(s)


s= 'monty pythons flying circus'
reversed_words(s)


s= 'monty pythons flying circus'
four_char_strings(s)
[vagrant@centos7-slave ~]$

