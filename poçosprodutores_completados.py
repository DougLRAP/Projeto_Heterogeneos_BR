import math


def distancia_euclidiana(point1, point2):
    if len(point1) != len(point2):
        raise ValueError("Points must have the same dimensionality")
    
    squared_distance = sum((x - y) ** 2 for x, y in zip(point1, point2))
    distance = math.sqrt(squared_distance)
    return distance

def ler_arquivo(nome_arquivo,r,z):
    blocos =[]
    blocos_total = 0
    ponto_central = (r//2,r//2)
    raio = r/2
    for a in range(0,r):
                blocos_linha = 0
                for b in range(0,r):
                    ponto = (a,b)
                    if distancia_euclidiana(ponto_central,ponto) <= raio:
                     blocos_total += 1
                     blocos_linha += 1
                blocos.append(blocos_linha)
    #bumps
    try:
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write(
                        f"WELL  'PRODUTOR 1'\n"
                        f"PRODUCER 'PRODUTOR 1'\n"
                        f"OPERATE  MIN  BHP  101.325  CONT \n"
                        f"**               rad      geofac    wfrac   skin\n"
                        f"GEOMETRY  J  0.1397  0.37  1.0  0.0  \n"
                        f"PERF      GEOA  'PRODUTOR 1'\n"
                        f"** UBA              ff          Status  Connection  \n"
                    )
            contador = 0
            for x in range(0,r):
                    for i in range(0,r):
                        ponto = (i,x)
                        if distancia_euclidiana(ponto_central,ponto) <= raio:
                            if contador == 0:
                                arquivo.write(
                                f"  {i+1} {z} {x+1}           -  OPEN    FLOW-TO  'SURFACE'\n"
                            )
                                contador +=1
                            else:
                                arquivo.write(
                                f"  {i+1} {z} {x+1}           -  OPEN    FLOW-TO  {contador}\n"
                            )
                                contador +=1
                    f"\n"
        print(f"Conteúdo foi escrito com sucesso no arquivo '{nome_arquivo}'.")
        
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")


if __name__ == "__main__":
    nome_do_arquivo = input("Digite o nome do arquivo para leitura: ")+'.inc'
    r = int(input("Digite o tamanho do grid na direção x: "))
    z = int(input("Digite o tamanho do grid na direção z: "))
    ler_arquivo(nome_do_arquivo,r,z)
 