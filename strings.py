
import pytest

mystring= 'monty pythons flying circus'

def no_duplicates(a_string):
    p= ""
    for char in a_string:
        if char not in p:
            p = p + char
    p= ''.join(sorted(p))
#    print(f" {p}")
    return p



def reversed_words(a_string):
    a_string= a_string.split(" ")
    a_string.reverse()
#    print(f" {a_string}")
    return a_string

def four_char_strings(a_string):
    n= 4
    chunks= []
    for i in range(0, len(a_string), n):
        chunks.append(a_string[i:i + n])
#    print(f" {chunks}")
    return chunks


def test_no_duplicates():
    s ='monty pythons flying circus'
    assert no_duplicates(s) == ' cfghilmnoprstuy'


def test_reversed_words():
    s= 'monty pythons flying circus'
    assert reversed_words(s) == ['circus', 'flying', 'pythons', 'monty']


def test_four_char_strings():
    s= 'monty pythons flying circus'
    assert four_char_strings(s) == ['mont', 'y py', 'thon', 's fl', 'ying', ' cir', 'cus']

