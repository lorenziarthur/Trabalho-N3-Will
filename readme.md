CADASTRO DE CARROS-Atividade N3 estrutura de dados 2 Semestre


# Sobre o projeto
Um sitema em python que guarda arquivos de carros em JSON, onde o usuário escolhe entre 5 opções no termimal quando estiver rodando o sistema


# Como executar
Rode no ternminal e escolhe entre as opções(1-Incluir um carro, 2-Alterar um carro, 3- Excluir um carro, 4-Pesquisar, 5-Listar), as opções são feitas a partir do ID, marca ou nome do carro


## Funcionalidades
1- Incluir: Solicita a marca, nome, premios e categoria, o novo ID vai ser calculado a partir do len(carros) + 1 e o carro vai ser adicionado na lista com o append
2- Alterar: Solicita o ID do carro, o laço (for c in carros), localiza o carro e pede os novos valores
3- Excluir: Solicita o ID do carro e remove o carro com (carros.remove(c))
4- Pesquisar: Solicita um texto cuja marca ou nome contenham esse texto
5- Lista: Exibe duas listas separadas por marca e categoria


## Como o programa salva os arquivos
Depois de cada operação, o programa salva a lista de carros no arquivo 'carros.json:
 with open("carros.json", "w", encoding="utf8") as f:
        json.dump({"data": carros}, f, ensure_ascii=False, indent=4)

O programa abre o arquivo, escreve nele todos os carros da lista e depois o fecha. Assim os dados continuam guardados mesmo após o sistema fechar. Quando o programa é iniciado ele lê o arquivo com 'json.load'.

# Tecnologias usadas
Pyhton para a parte do código
JSON para guardar os arquivos

