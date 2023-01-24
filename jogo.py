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