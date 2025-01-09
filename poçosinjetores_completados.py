import math

def distancia_euclidiana(point1, point2):
    if len(point1) != len(point2):
        raise ValueError("Points must have the same dimensionality")
    
    squared_distance = sum((x - y) ** 2 for x, y in zip(point1, point2))
    distance = math.sqrt(squared_distance)
    return distance

def ler_arquivo(nome_arquivo,r):
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
                        f"WELL  'INJE 1'\n"
                        f"INJECTOR MOBWEIGHT 'INJE 1'\n"
                        f"INCOMP  WATER\n"
                        f"OPERATE  MAX  STW  0.25 CONT\n"
                        f"OPERATE  MAX  BHP  1000  CONT\n"
                        f"**               rad      geofac    wfrac   skin\n"
                        f"*GEOMETRY  *J    1.125    0.37       1.00    0.0  \n"
                        f"PERF        WI  'INJE 1'\n"
                        f"** UBA             wi          Status  Connection  \n"
                    )
            contador = 0
            for x in range(0,r):
                    for i in range(0,r):
                        ponto = (i,x)
                        if distancia_euclidiana(ponto_central,ponto) <= raio:
                            if contador == 0:
                                arquivo.write(
                                f"  {i+1} 1 {x+1}           -  OPEN    FLOW-FROM  'SURFACE'\n"
                            )
                                contador +=1
                            else:
                                arquivo.write(
                                f"  {i+1} 1 {x+1}           -  OPEN    FLOW-FROM  {contador}\n"
                            )
                                contador +=1
                    f"\n"
            arquivo.write(
            f"\n"
            f"\n"
            f"\n"
            f"\n"
            f"\n"
            f"\n"
            )
            tempo = [600.0,1200.0,2160.0,3600.0,5040.0]
            vazao = [0.5,0.75,1.0,2.0,4.0]
            for j in range(0,len(vazao)):
                        arquivo.write(
                            f"\n"
                            f"  *TIME {tempo[j]}\n"
                            f"DTWELL 0.00166667\n"
                            f"  *ALTER 'INJE 1'\n"
                            f"  {vazao[j]}\n"
                        )
            arquivo.write(
                    f"\n"
                    f"  *TIME 7920.0\n"
            )
        print(f"Conteúdo foi escrito com sucesso no arquivo '{nome_arquivo}'.")
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")


if __name__ == "__main__":
    nome_do_arquivo = input("Digite o nome do arquivo para leitura: ") + '.inc'
    r = int(input("Digite o tamanho do grid na direção x: "))
    ler_arquivo(nome_do_arquivo,r)
 