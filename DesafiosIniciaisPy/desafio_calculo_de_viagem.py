"""
---------------------------------
Desafios Iniciais Py - Unimed-BH
---------------------------------
 Desafio 3/3 - Cálculo de viagem
---------------------------------
___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

Rubens quer calcular e mostrar a quantidade de litros de combustível gastos em uma viagem de carro, sendo que seu carro faz 12 KM/L. 
Como ele não sabe fazer um programa que o auxilie nessa missão, ele te pede ajuda. Para efetuar o cálculo, deve-se fornecer o tempo gasto em horas na viagem e a velocidade média durante a mesma em km/h. 
Assim, você conseguirá passar para Rubens qual a distância percorrida e, em seguida, calcular quantos litros serão necessários para a viagem que ele quer fazer. 
Mostre o valor com 3 casas decimais após o ponto.
____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

Parâmetros de entrada:
O arquivo de entrada contém dois inteiros. 
O primeiro é o tempo gasto na viagem em horas e o segundo é a velocidade média durante a mesma em km/h.

Parâmetros de saída:
Imprima a quantidade de litros necessária para realizar a viagem, com três dígitos após o ponto decimal


Dicas sobre os métodos fornecidas pela plataforma:
MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas

"""
valores = input().split()

tempo_gasto_em_horas = int(valores[0])
velocidade_media_kmh = int(valores[1])


distancia_percorrida_km = velocidade_media_kmh * tempo_gasto_em_horas           # Multiplicando o tempo de viagem pela velocidade média, tem-se a distancia percorrida em Km

qntd_litros_combustivel = distancia_percorrida_km / 12                          # Dividindo essa distância total pelo consumo em Km/L que o carro faz, tem-se a quantidade de combustivel necessária para viagem

qntd_litros_combustivel_float = f"{qntd_litros_combustivel:.3f}"                # Garantido que a saída atenderá aos criterios decimais do desafio

print(qntd_litros_combustivel_float)

# Saída mais bonitinha visualmente, mas para o desafio só pode constar o valor. --> print("A quantidade, em litros, de combustível necessária para viagem é:", qntd_litros_combustivel_float)

