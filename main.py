# titulo
t = 1
v1 = input("Loja 1: ")
v2 = input("Loja 2: ")
v3 = input("Loja 3: ")
v4 = input("Loja 4: ")
v5 = input("Loja 5: ")
v6 = input("Loja 6: ")
v7 = input("Loja 7: ")
v8 = input("Loja 8: ")
v9 = input("Loja 9: ")
v10 = input("Loja 10: ")
v11 = input("Loja 11: ")
v12 = input("Loja 12: ")
v13 = input("Loja 13: ")
v14 = input("Loja 14: ")
v15 = input("Loja 15: ")


storedic = {1: v1, 2: v2, 3: v3, 4: v4, 5: v5, 6: v6, 7: v7, 8: v8, 9: v9, 10: v10, 11: v11, 12: v12, 13: v13, 14: v14, 15: v15}

titulo = input("Digite seu título")

q = input("Deseja inserir um sufixo no texto também? (Y/N): ").upper()
if q == 'Y':
    texto1 = input("Digite a primeira parte de seu texto antes do sufixo aqui: ")
    texto2 = input("Digite a segunda parte de seu texto depois do sufixo aqui: ")
else:
    texto3 = input("Digite seu texto aqui: ")

while t != 16:
    sufixo = storedic.get(t)
    print(f"[{sufixo}] - {titulo}")

    if q == 'Y':
        print(f'{texto1} {sufixo} {texto2}')
    else:
        print(f'{texto3}')
    t += 1
