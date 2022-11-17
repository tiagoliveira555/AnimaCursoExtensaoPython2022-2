print('aula3-2022-11-09.py')
print()

from time import sleep

contador = 1

while (contador <= 10):
  print(contador)
  contador += 1
  sleep(1)
print()

print('Calcular imposto:')
def calcular_importo(valor):
  imposto = preco_produto * 0.05
  return imposto

preco_produto = 299

imposto = calcular_importo(preco_produto)
print(imposto)

def calcular_imposto_aliquota(valor, aliquota = 0.07):
  imposto = valor * aliquota
  return imposto