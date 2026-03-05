nomes = ["Ana", "Bruno", "Carlos", "Diana"]
print("Nomes ", nomes)

nomes.remove("Bruno")
print("Lista atualizada: ", nomes)

#removido = nomes.pop()
removido = nomes.pop(1)
print(f"Removido: {removido}")
print("Após pop(): ", nomes)

del nomes[0]
print("Após del nomes[0]:", nomes)

nomes.clear(
    print("lista atualizada:", nomes))
