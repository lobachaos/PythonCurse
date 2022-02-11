def func(*args,**kwargs):
    print(args)
    nome = kwargs.get('nome')
    if nome is not None:
     print(f'A variavel mandada na chave Nome foi --> {nome}')
    else:
        print(' Variavel Nome não  foi encontrada')


lista = [1,2,3,4,5,6]
listaB= [10,20,30,40]

func(lista,'outro argumento',5)
print('Desempacotando')
func(*lista,*listaB)
print('Localizando a variavel enviada')
func(1,2,3, nome='Samara')