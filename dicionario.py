# Dicionário é uma estrutura de dados que armazena coleções não ordenadas de pares chave-valor

#sem dicionário
matricula1 = 2026001
nome1 = "Ana Silva"
telefone1 = "9999-9999"

#com dicionario
aluno = [
matricula1 = 2026001
nome = "Ana Silva"
telefone = "9999-9999"
]

print(aluno)

contato = {
  "@camilaqueiroz": "Camila Queiroz",
  "@brunamarquezine": "Bruna M.",
  "@sheron Menezes": "Sheron M.",
  "@paolaoliveira": "Paola O.",
}
print(contato)
print(type(contato))

# Acesso Direto
print(contato{"@camilaqueiroz"})

# Acesso seguro com get()
print(contato.get("@paolaoliveira"))
print(contato.get("@inexistente"))
print(contato.get("@inexistente", "Não encontrado"))

# Add novo 
contato{"@giovanna"} = "Giovanna"
print("Após add: ", contato)

#Atualiza elemento existente
contato["@Paolaoliveira"] = "Paola Oliveira"
print("Após add: ", contato)

contato.update({
        "@brunamarquezine": "Bruna Marquezine",
        "@camilaqueiroz": "Camila Q."
})

print("Após Atualização: ", contato)

# Pop: Remove e retorna
removido = contato.pop("@paolaoliveira")
print(f"Removido: "(removido))
print("Após o pop: ", contato)

# del remove sem retornar
del contato["@camilaqueiroz"]
print("Após o del: ", contato)

#clear esvazia tudo
copia = dict(contato)
contato.clear()
print("Após clear: ", contato)
print("Cópia: ", copia)

print("Número de contato: ", len(contato)) #tamanho


# Verificar a existência

if "@joao" in contato:
    print(f"Econtrado: {contato['@joao']}")

if "@inexistente" in contato:
    print("Existe")
else:
    print("Não existe.")