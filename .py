#GERADOR DE TABUADA

print('---GERADOR DE TABUADA---'.center(40))
print('\n')

operacao = input('(+)/(-)/(*)/(/): ')

print('\n')

if operacao == '+':

  numero = int(input('Tabuada do: '))
  print('\n')

  for i in range(1, 101):
    resultado = numero + i
    print(f'{numero} + {i} = {resultado}')

elif operacao == '-':

  numero = int(input('Tabuada do: '))
  print('\n')

  for i in range(1, 101):
    resultado = numero - i
    print(f'{numero} - {i} = {resultado}')

elif operacao == '*':

  numero = int(input('Tabuada do: '))
  print('\n')

  for i in range(1, 101):
    resultado = numero * i
    print(f'{numero} X {i} = {resultado}')

elif operacao == '/':

  numero = int(input('Tabuada do: '))
  print('\n')

  for i in range(1, 101):
    resultado = numero / i
    print(f'{numero} / {i} = {resultado:2f}')

else:

  print('Operação Inválida!')
