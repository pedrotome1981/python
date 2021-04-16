numeroSecreto = 5
adivinha = 0

while adivinha != numeroSecreto:
    adivinha= int(input("adivinha o numero entre 1 e 10: "))

if adivinha == numeroSecreto:
    print("Acertaste, é o número 5.")
else:
    print("Lamento, mas o " + str(adivinha) + " não é o número correcto!")