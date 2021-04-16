nome = input("Olá, como te chamas?")
print("Olá " + nome + ", muito prazer. Eu sou a SmartNinja.")

nota = input("Podes avaliar as aulas da SmartNinja? 1 = mau até 5 = bom")
print("A tua escolha foi: " + nota)

if nota == "1":
    print("Erro! O sistema apenas aceita notas acima de 3!")

elif nota == "2":
    print("Erro! O sistema apenas aceita notas acima de 3!")
elif nota == "3":
    print("Médio!? Não queres rever a tua nota?")
elif nota == "4":
    print("Boa, assim mesmo!")
elif nota == "5":
    print("Excelente, nós tambem te adoramos")
else:
    print("Essa nota não foi reconhecida. Não sabes contar? 1.. 2.. 3.. 4.. 5..")


