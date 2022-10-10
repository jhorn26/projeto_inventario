dicionario = {}

def listar_inventario(dicionario):
    print("Inventário:\n")
    for key in dicionario.keys():
        print(key, ":", dicionario[key])


def adiciona_item(dicionario, item, quantidade):
    dicionario[item]=quantidade
    
    return dicionario


def remove_item(dicionario, item):
    dicionario.pop(item)

    return dicionario

def busca_item():
    pass



dicionario = adiciona_item(dicionario, "flauta", 10)
dicionario = adiciona_item(dicionario, "violao", 20)
print(dicionario)
dicionario = remove_item(dicionario, "guitarra")

print(dicionario)


