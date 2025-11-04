"""
Desafio: Criar uma calculadora estatística simples em Python

Tarefa:
Implemente as funções abaixo para calcular média, mediana e moda de uma lista de números.

Instruções:
1. Faça o fork deste repositório no seu GitHub.
2. Clone o seu fork para sua máquina.
3. Complete as funções abaixo.
4. Teste o código executando: python calculadora_estatistica.py
5. Envie um Pull Request com a sua solução.

💡 Dica: não use bibliotecas externas como numpy ou statistics.
"""

# Função para calcular a média
def calcular_media(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

# Função para calcular a mediana
def calcular_mediana(lista):
    lista_ordenada = sorted(lista)
    tamanho = len(lista_ordenada)
    
    if tamanho % 2 == 0:  # Se o tamanho da lista for par
        meio1 = lista_ordenada[tamanho // 2 - 1]
        meio2 = lista_ordenada[tamanho // 2]
        return (meio1 + meio2) / 2
    else:  # Se o tamanho da lista for ímpar
        return lista_ordenada[tamanho // 2]

# Função para calcular a moda
def calcular_moda(lista):
    ocorrencias = {}
    
    for num in lista:
        if num in ocorrencias:
            ocorrencias[num] += 1
        else:
            ocorrencias[num] = 1
    
    # Encontra o número com mais ocorrências
    maior_ocorrencia = max(ocorrencias.values())
    moda = [num for num, freq in ocorrencias.items() if freq == maior_ocorrencia]
    
    # Se mais de um número tiver a mesma maior ocorrência, retornamos todos.
    return moda

def main():
    try:
        numeros = [10, 20, 20, 30, 40, 40, 40, 50]

        print("Calculadora Estatística")
        print(f"Lista de números: {numeros}")
        print(f"Média: {calcular_media(numeros)}")
        print(f"Mediana: {calcular_mediana(numeros)}")
        print(f"Moda: {calcular_moda(numeros)}")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")


if __name__ == "__main__":
    main()
