#!/usr/bin/env python

def KSA(chave):
    chave_tamanho = len(chave)

    S = range(256)

    j = 0
    for i in range(256):
        j = (j + S[i] + chave[i] % chave_tamanho]) % 256
        S[i], S[j] = S[j], S[i]  # swap

    return S


def PRGA(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]  # swap

        K = S[(S[i] + S[j]) % 256]
        yield K


def RC4(chave):
    S = KSA(chave) #S recebe o KSA da chave (Vetor de inicialização)
    return PRGA(S) #Retorna S para o PRGA


if __name__ == '__main__':

    chave = 'chave'
    texto_claro = 'texto_claro'

    def letra_to_ascii(s):
        return [ord(c) for c in s]
    
    chave = letra_to_ascii(chave)

    chavestream = RC4(chave)

    import sys
    
    for c in texto_claro:
        sys.stdout.write("%02X" % (ord(c) ^ chavestream.next()))
    
    print
