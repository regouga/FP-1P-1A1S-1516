# P1 - FP // Miguel Regouga, 83530 // Paulo Reves, 83537 // Grupo 38


# Funcoes Auxiliares

# A funcao 'soma_tuplos' devolve a soma de dois tuplos com o mesmo numero de elementos.

def soma_tuplos (tuplo1, tuplo2):
    i = 0
    tuplo_soma = ()
    tamanho_tuplo = len(tuplo1)
    while i < tamanho_tuplo:
        soma = tuplo1[i] + tuplo2[i]
        i = i + 1
        tuplo_soma = tuplo_soma + (soma, )
    return tuplo_soma            
            




# Questao 1

# Comeca-se por transformar o tuplo 'nr_votos' numa lista, pois estas sao mutaveis 
# e tornam o processo mais simples de programar.

# A variavel 'res' e uma lista que tem o mesmo numero de elementos da lista 'nr_votos', 
# sendo que estes tem todos o valor 0 inicialmente. 

# O ciclo for vai percorrer todos os indices, e vai encontrar aquele cujo valor e o maior, 
# de modo a atribuir o mandato a essa mesma candidatura, sem alterar a posicao inicial presente no tuplo 'nr_votos'. 
# O processo e repetido ate so haver um maximo.

# Caso existam dois valores iguais, ou seja, 'dois maximos', o mandato e atribuido 
# a canditatura cujo numero de votos inicial foi o menor, o que esta representado na instrucao de selecao 'elif'.

# A medida que sao descobertos os maximos, vai-se adicionando 1 mandato a respetiva candidatura e 
# divide-se esse mesmo maximo por x+1, sendo que x corresponde ao numero de divisoes ja feitas.

# E pretendido que o resultado seja um tuplo, e nao uma lista, e por isso, no final, converte-se a lista 'res' para tuplo.


def mandatos (nr_mandatos, nr_votos):
    lista_votos = list(nr_votos)
    tamanho_nr_votos = (len(nr_votos))
    res = [] + tamanho_nr_votos * [0]
    nr_mandatos_atuais = 0
    
    while nr_mandatos_atuais < nr_mandatos:
        max_nr_votos = 0
        for i in range (len(lista_votos)):
            if lista_votos[i] > lista_votos[max_nr_votos]:
                max_nr_votos = i
            elif lista_votos[i] == lista_votos[max_nr_votos]:
                if nr_votos[i] < nr_votos[max_nr_votos]:
                    max_nr_votos = i
                

        res[max_nr_votos] = (res[max_nr_votos] + 1)
        lista_votos[max_nr_votos] = nr_votos[max_nr_votos] / (res[max_nr_votos] + 1)
        nr_mandatos_atuais = nr_mandatos_atuais + 1       
    
    return tuple(res)





# Questao 2
    
# O tuplo 'nr_mandatos_circ_elei' corresponde ao numero de mandatos a atribuir a cada circulo eleitoral.
# Este tuplo esta ordenado de acordo com a ordem da tabela 1.

# Pretende-se o numero de mandatos atribuidos a cada candidatura na Assembleia da Republica. 
# Para tal, e primeiramente aplicada a funcao 'mandatos' (definida na questao 1) a cada circulo eleitoral - variavel 'mandatos_circ_elei'.

# Tendo o numero de mandatos atribuido a cada candidatura nos 22 circulos eleitorais, somam-se esses mesmos mandatos, com o objetivo de obter o pretendido. 
# Para tal, e utilizada a funcao 'soma_tuplos'. Este ultimo passo corresponde a variavel 'resultado'.


def assembleia(votacoes):
    nr_mandatos_circ_elei = (16, 3, 19, 3, 4, 9, 3, 9, 4, 10, 47, 2, 39, 9, 18, 6, 5, 9, 5, 6, 2, 2)
    resultado = (0,) * 15
    for i in range(len(nr_mandatos_circ_elei)):
        mandatos_circ_elei = mandatos(nr_mandatos_circ_elei[i], votacoes[i])
        resultado = soma_tuplos(resultado, mandatos_circ_elei)
    return resultado




       
# Questao 3

# A variavel 'partidos' corresponde ao tuplo com o nome das 15 candidaturas.
# Este tuplo esta ordenado de acordo com a tabela 2.

# E utilizado novamente um ciclo for para percorrer os elementos do tuplo da variavel 'resultados'. 
# Estes vao sendo analisados, e ao percorrer o tuplo, vai sendo guardado o indice do maximo atual. 


def max_mandatos (votacoes):
    partidos = ('PDR\tPartido Democratico Republicano',\
                'PCP-PEV\tCDU - Coligacao Democratica Republicana',\
                'PPD/PSD-CDS/PP\tPortugal a Frente',\
                'MPT\tPartido da Terra',\
                'L/TDA\tLivre/Tempo de Avancar',\
                'PAN\tPessoas-Animais-Natureza',\
                'PTP-MAS\tAgir',\
                'JPP\tJuntos Pelo Povo',\
                'PNR\tPartido Nacional Renovador',\
                'PPM\tPartido Popular Monarquico',\
                'NC\tNos, Cidadaos!',\
                'PCTP/MRPP\tPartido Comunista dos Trabalhadores Portugueses',\
                'PS\tPartido Socialista',\
                'B.E.\tBloco de Esquerda',\
                'PURP\tPartido Unido dos Reformados e Pensionistas')
    resultados = assembleia(votacoes)
    
    empate = False
    
    max_ind = 0
    for i in range(len(resultados)):
        if resultados[i] > resultados[max_ind]:
            max_ind = i
            empate = False
        elif i != max_ind and resultados[i] == resultados[max_ind]:
            # Caso se encontre um indice diferente do indice do maximo, 
            # mas com valores correspondentes iguais, e registado que ha um empate. 
            empate = True
            
    if empate:
        return 'Empate tecnico'
    # Se os valores desse mesmo empate sao tambem os maximos, e dada a mensagem de empate tecnico. 
    else:
        return partidos[max_ind]
    # Caso contrario, a funcao 'max_mandatos' devolve o nome da candidatura que ganhou. 