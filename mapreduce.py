import operator, os

listas = ["Michelle", "Eduardo", "Will"] #De strings
listan = [4, 6, 8, 10]			 #De Numero
listaf = [4.78, 6.78, 8.78, 10.78]	 #De float
listac = ["M","E","W"]			 #De Char
listam = ["Gabriel", 654, 4.78, "M"]	 #Mista

lamb = lambda x: x*2 #Funcao usada no map que multiplica por 2

os.system("clear")
print "====		Valores insediros			===="

print listas;print listan; print listaf; print listac; print listam

print "====		Valores de MAP(elevando a 2);SORT	===="


"""

Implementacao do MAP e SORT

"""

#resposta do map de strings
rmaps = map(lamb, listas)

print sorted(rmaps)

#resposta do map de numbers
rmapn = map(lamb, listan)

print sorted(rmapn)

#resposta do map de floats
rmapf = map(lamb, listaf)

print sorted(rmapf)

#resposta do map de char
rmapc = map(lamb, listac)

print sorted(rmapc)

#resposta do map misto
rmapm = map(lamb, listam)

print sorted(rmapm)

"""

Implementacao do REDUCE dos valores insediros

"""

print"====		Valores do Reduce (iserido (soma))	===="

#Resposta do reduce de string 
rreds = reduce(operator.add, listas)

print rreds
#Resposta do reduce de Number
rredn = reduce(operator.add, listan)

print rredn
#Resposta do reduce de Float 
rredf = reduce(operator.add, listaf)

print rredf
#Resposta do reduce de char 
rredc = reduce(operator.add, listac)

print rredc

#Problema: Nao podemos concatenar inteiros e strings
	
"""
	#Resposta do reduce misto 
	rredm = reduce(operator.add, listam)

	print rredm
"""

print "FAIL: MISTO"
"""

Implementacao do REDUCE dos valores mapeados

"""

print"====		Valores do Reduce (mapeados (soma))	===="

#Resposta do reduce de string 
rreds = reduce(operator.add, rmaps)

print rreds
#Resposta do reduce de Number
rredn = reduce(operator.add, rmapn)

print rredn
#Resposta do reduce de Float 
rredf = reduce(operator.add, rmapf)

print rredf
#Resposta do reduce de char 
rredc = reduce(operator.add, rmapc)

print rredc

#Problema: Nao podemos concatenar inteiros e strings
"""
	#Resposta do reduce misto 
	rredm = reduce(operator.add, listam)

	print rredm
"""
print "FAIL: MISTO"
