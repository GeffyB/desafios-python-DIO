"""
---------------------------------------
Desafios Intermediários Py - Unimed-BH
   ---------------------------------
    Desafio 3/3 - Aumento Salarial
   ---------------------------------
___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

A empresa que você trabalha resolveu conceder um aumento salarial a todos funcionários, de acordo com a tabela abaixo:
Salário             |Percentual de Reajuste
0 - 600.00          |17%
600.01 - 900.00     |13%
900.01 - 1500.00    |12%
1500.01 - 2000.00   |10%
Acima de 2000.00    |5%

Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.

____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

Parâmetros de entrada:
A entrada contém apenas um valor de ponto flutuante, que pode ser maior ou igual a zero, com duas casas decimais, conforme exemplos abaixo.

Parâmetros de saída:
Novo salario: 1120,00 
Reajuste ganho: 120,00                                                                                     
Em percentual: 12 %

FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, onde geralmente informa que tipo de informação ele está esperando receber;
FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas em cada parâmetro da função ou com os valores predefinidos por padrão;

"""
# Abaixo segue um exemplo de código que você pode ou não utilizar
salario = int(input())                                # input("Digite seu salário atual") fica mais bonitinho mas dá erro na plataforma do desafio

if (salario <= 600):
   novo_salario = salario + (salario * (17/100))
   reajuste_ganho = novo_salario - salario
   em_percentual = 17
   print("Novo salario:", "{:.2f}".format(novo_salario))          # Dá pra fazer esse print todo usando uma única F-string ao fim do script
   print("Reajuste ganho:", "{:.2f}".format(reajuste_ganho))
   print("Em percentual:", em_percentual, "%")

elif (salario >=600.01 and salario <=900):
   novo_salario = salario + (salario * (13/100))
   reajuste_ganho = novo_salario - salario
   em_percentual = 13
   print("Novo salario:", "{:.2f}".format(novo_salario))
   print("Reajuste ganho:", "{:.2f}".format(reajuste_ganho))
   print("Em percentual:", em_percentual, "%")

elif (salario >=900.01 and salario <=1500):
   novo_salario = salario + (salario * (12/100))
   reajuste_ganho = novo_salario - salario
   em_percentual = 12
   print("Novo salario:", "{:.2f}".format(novo_salario))
   print("Reajuste ganho:", "{:.2f}".format(reajuste_ganho))
   print("Em percentual:", em_percentual, "%")

elif (salario >=1500.01 and salario <=2000):
   novo_salario = salario + (salario * (10/100))
   reajuste_ganho = novo_salario - salario
   em_percentual = 10
   print("Novo salario:", "{:.2f}".format(novo_salario))
   print("Reajuste ganho:", "{:.2f}".format(reajuste_ganho))
   print("Em percentual:", em_percentual, "%")

else: 
   novo_salario = salario + (salario * (5/100))
   reajuste_ganho = novo_salario - salario
   em_percentual = 5
   print("Novo salario:", "{:.2f}".format(novo_salario))
   print("Reajuste ganho:", "{:.2f}".format(reajuste_ganho))
   print("Em percentual:", em_percentual, "%")


# TODO:  Calcule o salário do funcionário e print o novo salário, bem como o valor de reajuste ganho e o índice reajustado (em porcentagem)
