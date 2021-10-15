# titulo
t = 1
v1 = input("Loja 1: ")
v2 = input("Loja 2: ")
v3 = input("Loja 3: ")
v4 = input("Loja 4: ")
v5 = input("Loja 5: ")

storedic = {1: v1, 2: v2, 3: v3, 4: v4, 5: v5}

titulo = input("Digite seu título")

q = input("Deseja inserir um sufixo no testo também? (Y/N): ").upper()
if q == 'Y':
    texto1 = input("Digite a primeira parte de seu texto antes do sufixo aqui: ")
    texto2 = input("Digite a segunda parte de seu texto depois do sufixo aqui: ")
else:
    texto3 = input("Digite seu texto aqui: ")

while t != 6:
    sufixo = storedic.get(t)
    print(f"[{sufixo}] - {titulo}")

    if q == 'Y':
        print(f'{texto1} {sufixo} {texto2}')
    else:
        print(f'{texto3}')
    t += 1
