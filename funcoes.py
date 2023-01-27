def define_posicoes(linha,coluna,orientacao,tamanho):
    posicoes=[]
    i=0
    
    while i < tamanho:
        if orientacao == 'horizontal':
            posicoes.append([linha,coluna+i])
        if orientacao == 'vertical':
            posicoes.append([linha+i,coluna])
        i+=1
    return posicoes

def preenche_frota(frota,nome,linha,coluna,orientacao,tamanho):
    if nome not in frota:
        frota[nome]=[define_posicoes(linha,coluna,orientacao,tamanho)]

    else:
        frota[nome].append(define_posicoes(linha,coluna,orientacao,tamanho))
        
    return frota

def faz_jogada(tabuleiro,linha,coluna):
    if tabuleiro[linha][coluna] == 1:
       tabuleiro[linha][coluna] = 'X'
    
    if tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro

def posiciona_frota(dic):
    lista=[
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
    for navio, listap in dic.items():
        for posicoes in listap:
            for posicao in posicoes:
                x=posicao[0]
                y=posicao[1]
                lista[x][y]=1
    return lista

def afundados(dic,tabuleiro):
    afundados=0
    afundado=False
    for nome, listap in dic.items():
        for barco in listap:
            if afundado==True:
                afundados+=1
            afundado=False
            for posicoes in barco:
                x=posicoes[0]
                y=posicoes[1]
                if tabuleiro[x][y]=='X':
                    afundado=True
                else:
                    afundado=False
                    break
    if afundado==True:
        afundados+=1
    return afundados