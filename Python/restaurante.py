class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Bistrô'
restaurante_praca.categoria = 'Italiana'

nome_do_restaurante = restaurante_praca.nome
if restaurante_praca.ativo:
    print('O restaurante está ativo.')
else: 
    print('O restaurante está inativo.')

categoria = Restaurante.categoria

restaurante_pizza = Restaurante()

restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'
if restaurante_pizza.categoria == 'Fast Food':
    print('a categoria e fast food.')
else:
    print('a categoria nao e fast food.')

restaurante_pizza.ativo = True

restaurantes = [restaurante_praca, restaurante_pizza]

print(f'Nome: {restaurante_praca.nome}, Categoria: {restaurante_praca.categoria}')