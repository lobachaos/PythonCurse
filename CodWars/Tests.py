string = "q, w, e, r, t, a, s, d, f, g, z, x, c, v, b"
string_entrada = "wyer"

lista = string.split(', ')
print(len(lista))

string_nova = ''

for letra in string_entrada:
    if letra in lista:
        string_nova += 'left'
    else:
        string_nova += 'right'

print(string_nova)

if string_nova.__contains__('leftleft') or string_nova.__contains__('rightright'):
    print("Not Confortable")
else:
    print("Confortable")
