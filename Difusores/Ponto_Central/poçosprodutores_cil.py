import math


def distancia_euclidiana(point1, point2):
    if len(point1) != len(point2):
        raise ValueError("Points must have the same dimensionality")
    
    squared_distance = sum((x - y) ** 2 for x, y in zip(point1, point2))
    distance = math.sqrt(squared_distance)
    return distance


def ler_arquivo(nome_arquivo,r,z):
    poços = 0
    ponto_central = (r//2,r//2)
    print(f"o ponto central é '{ponto_central}'")
    raio = r/2
    for a in range(0,r):
                for b in range(0,r):
                    ponto = (a,b)
                    if distancia_euclidiana(ponto_central,ponto) <= raio:
                      var_x = ponto_central[1]
                      if ponto[1] < var_x:
                         poços += 1
    try:
        with open(nome_arquivo, 'w') as arquivo:
            contador = 0
            for j in range(0,r):
                for i in range(0,r):
                    ponto = (i,j)
                    if distancia_euclidiana(ponto_central,ponto) <= raio:
                         #ponto central tem (y,x)
                        var_x = ponto_central[1]
                        if ponto[1] < var_x:
                            arquivo.write(
                                f"WELL  'PRODUTOR {contador+1}'\n"
                                f"PRODUCER 'PRODUTOR {contador+1}'\n"
                                f"OPERATE  MIN  BHP  101.325  CONT \n"
                                f"**               rad      geofac    wfrac   skin\n"
                                f"GEOMETRY  J  0.1397  0.37  1.0  0.0  \n"
                                f"PERF      GEOA  'PRODUTOR {contador+1}'\n"
                                f"** UBA              ff          Status  Connection  \n"
                                f"{j+1} {z} {i+1}      1.0  OPEN    FLOW-TO  'SURFACE'\n"
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
    z = int(input("Digite o tamanho do grid na direção z: "))
    ler_arquivo(nome_do_arquivo,r,z)
 