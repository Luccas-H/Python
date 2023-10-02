preco_base = float(input("Digite o preço de fabrica do veiculo: "))
lucro_percentual = float(input("Digite o percentual de lucro: "))
imposto = float(input("Digite o percentual de imposto: "))

print('O valor de lucro do distribuidor é {}, o valor pago de imposto é {} e o preço final do veiculo é {} '.format(preco_base*(lucro_percentual/100), preco_base*(imposto/100),(preco_base*(lucro_percentual/100) + preco_base) + preco_base*(imposto/100) ))