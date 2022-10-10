
"""
---------------------------------------
Desafios Intermediários Py - Unimed-BH
   ---------------------------------
   Desafio 2/3 - Papagaio Poliglota
   ---------------------------------
___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

Humberto tem um papagaio muito esperto. 
Quando está com as duas pernas no chão, o papagaio fala em português. 
Quando levanta a perna esquerda, fala em inglês. Por fim, quando levanta a direita fala em francês. 
Nico, amigo de Humberto, ficou fascinado com o animal. Em sua emoção perguntou: “E quando ele levanta as duas?”. 
Antes que Humberto pudesse responder, o papagaio gritou: “Aí eu caio, idiota!”.

____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

Parâmetros de entrada:
A entrada consiste de diversos casos de teste. Cada caso de teste consiste uma string informando qual a situação de levantamento de pernas do papagaio.

Parâmetros de saída:
Para cada condição de levantamento de pernas do papagaio, imprima a linguagem que ele utilizará. Caso ele levante ambas as pernas, imprima “caiu”. 
Quebre uma linha a cada caso de teste.


Dicas fornecidas pela plataforma:
FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, onde geralmente informa que tipo de informação ele está esperando receber;
FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas em cada parâmetro da função ou com os valores predefinidos por padrão;
while True significa que, enquanto houver entradas, o código após o try continuará sendo executado

Exemplo de Entrada|Exemplo de Saída
esquerda          |  ingles
                  |  
direita           |  frances
                  | 
nenhuma           |  portugues
                  | 
ambas             | caiu

"""
# perna = input() Se essa declaração for feita fora do laço while, é necessário adicionar um break por condição ou o terminal rodará em loop com a saida quando executado


while True: 
    try:
        perna = input() 
           
        if perna == "esquerda":
            print("ingles \n")                 # Nota: A entrada e saída precisa respeitar as condições do desafio (letras maiusculas ou miusculas) caso contrario retorna erro
            #break

        elif perna == "direita":
            print("frances \n")
            #break

        elif perna == "nenhuma":
            print("portugues \n")
            #break

        elif perna == "ambas":
            print("caiu \n")
            #break

    except EOFError: 
        break