nome = input("Informe seu nome: ")
nota = float(input("Digite sua nota: "))

if (nota == 10):
  print(f"{nome}, você é o bichão, mesmo...")
elif (nota >= 6 and nota < 10):
  print(f"{nome}, bom trabalho...")
else:
  print("Burro, não tirou dez...")