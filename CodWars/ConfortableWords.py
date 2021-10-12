"""
https://www.codewars.com/kata/56684677dc75e3de2500002b
A comfortable word is a word which you can type always alternating the hand you type with
(assuming you type using a QWERTY keyboard and use fingers as shown in the image below).

That being said, complete the function which receives a word and returns true if it's a comfortable word a
nd false otherwise.

The word will always be a string consisting of only ascii letters from a to z.
To avoid problems with image availability, here's the lists of letters for each hand:

    Left: q, w, e, r, t, a, s, d, f, g, z, x, c, v, b
    Right: y, u, i, o, p, h, j, k, l, n, m

Examples

"yams"  -->  true
"test"  -->  false

"""


def comfortable_word(string):
    string_left = "q, w, e, r, t, a, s, d, f, g, z, x, c, v, b"
    string_entrada = string

    lista_left = string_left.split(', ')

    string_nova = ''

    for letra in string_entrada:
        if letra in lista_left:
            string_nova += 'left'
        else:
            string_nova += 'right'

    if string_nova.__contains__('leftleft') or string_nova.__contains__('rightright'):
        return False
    else:
        return True


def comfortable_word2(word):
    left = [c in 'qwertasdfgzxcvb' for c in word[::2]]
    right = [c in 'yuiophjklnm' for c in word[1::2]]

    return (all(left) and all(right)) or (not any(left) and not any(right))
