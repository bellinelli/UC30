distancia = 450
consumo_carro = 8
preco_litro = 5.50

litros_consumidos = distancia / consumo_carro
custo_total = litros_consumidos * preco_litro

print("Distância percorrida:", distancia, "km")
print("Consumo do carro:", consumo_carro, "km/l")
print("Litros consumidos:", litros_consumidos)
print("Custo total do combustível: R$", custo_total)