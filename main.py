import json

with open("carros.json", encoding="utf8") as f:
    carros = json.load(f)["data"]

while True:
    print("\n1-Incluir 2-Alterar, 3-Excluir 4-Pesquisar 5-Listar 0-Sair")
    op = input("Opcao: ")

    if op == "1":
        novo_id = len(carros) + 1
        marca = input("Marca: ")
        nome = input("Nome: ")
        premios = input("Premios: ")
        categoria = input("Categoria: ")
        carros.append({"id": novo_id, "Marca": marca, "Nome": nome, "Premios": premios, "Categoria": categoria})

    elif op == "2":
        id = int(input("ID: "))
        for c in carros:
            if c["id"] == id:
                c["Marca"] = input("Nova marca: ")
                c["Nome"] = input("Novo nome: ") 
                c["Premios"] = input("Novos premios: ")
                c["Categoria"] = input("Noca categoria: ")



    elif op == "3":
        id = int(input("ID: "))
        for c in carros:
            if c["id"] == id:
                carros.remove(c)


    elif op == "4":
        texto = input("Pesquisar: ").lower()
        for c in carros:
            if texto in c["Marca"].lower() or texto in c["Nome"].lower():
                print(c["id"], c["Marca"], c["Nome"], c["Premios"], c["Categoria"])




    elif op == "5":
        print("--- Por marca ---")
        for c in sorted(carros, key=lambda c: c["Marca"]):
            print(c["Marca"], c["Nome"])
        print("--- Por categoria ---") 
        for c in sorted(carros, key=lambda c: c["Categoria"]):
            print(c["Categoria"], c["Nome"])

    elif op == "0":
        break

    with open("carros.json", "w", encoding="utf8") as f:
        json.dump({"data": carros}, f, ensure_ascii=False, indent=4)

