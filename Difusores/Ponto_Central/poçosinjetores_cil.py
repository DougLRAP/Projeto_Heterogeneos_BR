import math


def distancia_euclidiana(point1, point2):
    if len(point1) != len(point2):
        raise ValueError("Points must have the same dimensionality")
    
    squared_distance = sum((x - y) ** 2 for x, y in zip(point1, point2))
    distance = math.sqrt(squared_distance)
    return distance


def ler_arquivo(nome_arquivo,r):
    poços = 0
    ponto_central = (r//2,r//2)
    print(f"o ponto central é '{ponto_central}'")
    
    try:
        with open(nome_arquivo, 'w') as arquivo:
            contador = 0
            arquivo.write(
                                f"WELL  'INJE {contador+1}'\n"
                                f"INJECTOR MOBWEIGHT 'INJE {contador+1}'\n"
                                f"INCOMP  WATER\n"
                                f"OPERATE  MAX  STW  .25 CONT\n"
                                f"OPERATE  MAX  BHP  1000  CONT\n"
                                f"**               rad      geofac    wfrac   skin\n"
                                f"*GEOMETRY  *J    1.125    0.37       1.00    0.0  \n"
                                f"PERF        WI  'INJE {contador+1}'\n"
                                f"** UBA             wi          Status  Connection  \n"
                                f"{ponto_central[0]} 1 {ponto_central[1]}           -  OPEN    FLOW-FROM  'SURFACE'\n"
                                f"\n"
                            )
            contador += 1
        print(f"Conteúdo foi escrito com sucesso no arquivo '{nome_arquivo}'.")
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
    print(f"O número total de poços é '{poços}")


if __name__ == "__main__":
    nome_do_arquivo = input("Digite o nome do arquivo para leitura: ")
    r = int(input("Digite o tamanho do grid na direção x: "))
    ler_arquivo(nome_do_arquivo,r)
 